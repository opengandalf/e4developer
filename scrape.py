#!/usr/bin/env python3
"""Scrape e4developer.com WordPress site and convert to Hugo content."""

import os
import re
import sys
import time
import hashlib
import subprocess
import urllib.parse
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify as md, MarkdownConverter

BASE_URL = "https://www.e4developer.com"
SITEMAP_URL = f"{BASE_URL}/sitemap-1.xml"
CONTENT_DIR = Path("content/posts")
SKIP_PATHS = {
    "/log-in/", "/sign-up/", "/reset-password/", "/account/",
    "/my-profile/", "/member-directory/", "/contact/", "/start-here/"
}


def curl_fetch(url, binary=False, timeout=30):
    """Fetch a URL using curl (bypasses Python SSL/WAF issues)."""
    cmd = ["curl", "-sL", "--max-time", str(timeout), url]
    result = subprocess.run(cmd, capture_output=True, timeout=timeout + 10)
    if result.returncode != 0:
        raise Exception(f"curl failed for {url}: {result.stderr.decode()}")
    if binary:
        return result.stdout
    return result.stdout.decode("utf-8", errors="replace")


class CustomConverter(MarkdownConverter):
    """Custom markdownify converter that preserves code blocks with language tags."""

    def convert_pre(self, el, text, parent_tags=None):
        code_el = el.find("code")
        if code_el:
            lang = ""
            classes = code_el.get("class", [])
            if isinstance(classes, str):
                classes = classes.split()
            for cls in classes:
                if cls.startswith("language-"):
                    lang = cls.replace("language-", "")
                    break
                elif cls.startswith("lang-"):
                    lang = cls.replace("lang-", "")
                    break
            # Also check data-enlighter-language attribute
            if not lang:
                lang_attr = code_el.get("data-enlighter-language", "")
                if lang_attr:
                    lang = lang_attr
            if not lang:
                lang_attr = el.get("data-enlighter-language", "")
                if lang_attr:
                    lang = lang_attr
            # Get raw text content
            code_text = code_el.get_text()
            lines = code_text.split("\n")
            while lines and not lines[0].strip():
                lines.pop(0)
            while lines and not lines[-1].strip():
                lines.pop()
            code_text = "\n".join(lines)
            return f"\n\n```{lang}\n{code_text}\n```\n\n"
        # Fallback: treat as generic code block
        text = el.get_text()
        return f"\n\n```\n{text}\n```\n\n"

    def convert_img(self, el, text, parent_tags=None):
        alt = el.get("alt", "")
        src = el.get("src", "") or el.get("data-src", "")
        if not src:
            return ""
        return f"![{alt}]({src})"

    def convert_figure(self, el, text, parent_tags=None):
        img = el.find("img")
        if img:
            return self.convert_img(img, text, parent_tags)
        return text


def custom_md(html, **kwargs):
    return CustomConverter(**kwargs).convert(html)


def fetch_sitemap():
    """Fetch and parse the sitemap XML."""
    print("Fetching sitemap...")
    xml_text = curl_fetch(SITEMAP_URL)
    soup = BeautifulSoup(xml_text, "lxml-xml")
    urls = []
    for loc in soup.find_all("loc"):
        url = loc.text.strip()
        urls.append(url)
    print(f"Found {len(urls)} URLs in sitemap")
    return urls


def should_skip(url):
    """Check if URL should be skipped."""
    path = urllib.parse.urlparse(url).path
    for skip in SKIP_PATHS:
        if path == skip or path.rstrip("/") == skip.rstrip("/"):
            return True
    # Skip the home page
    if path == "/" or path == "":
        return True
    return False


def extract_date_from_url(url):
    """Extract date from URL path like /2018/01/13/slug/."""
    path = urllib.parse.urlparse(url).path
    match = re.search(r"/(\d{4})/(\d{2})/(\d{2})/", path)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}T00:00:00Z"
    return None


def extract_slug_from_url(url):
    """Extract slug from URL path."""
    path = urllib.parse.urlparse(url).path.strip("/")
    parts = path.split("/")
    # For date-based URLs: /2018/01/13/slug/ -> slug
    if len(parts) >= 4 and re.match(r"\d{4}", parts[0]):
        return parts[-1]
    # For other URLs, use last segment
    return parts[-1] if parts else "unknown"


def download_image(img_url, post_dir):
    """Download an image and return local path."""
    images_dir = post_dir / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    # Parse the image filename
    parsed = urllib.parse.urlparse(img_url)
    filename = os.path.basename(parsed.path)
    if not filename or filename == "/":
        # Generate filename from URL hash
        filename = hashlib.md5(img_url.encode()).hexdigest()[:12] + ".jpg"

    # Clean filename
    filename = re.sub(r'[^\w\-.]', '_', filename)
    local_path = images_dir / filename

    if local_path.exists():
        return f"images/{filename}"

    try:
        data = curl_fetch(img_url, binary=True)
        with open(local_path, "wb") as f:
            f.write(data)
        return f"images/{filename}"
    except Exception as e:
        print(f"  WARNING: Failed to download image {img_url}: {e}")
        return None


def rewrite_image_urls(markdown_text, img_map):
    """Replace remote image URLs with local paths."""
    for remote_url, local_path in img_map.items():
        if local_path:
            markdown_text = markdown_text.replace(remote_url, local_path)
    return markdown_text


def extract_article(url):
    """Fetch and extract article content from a URL."""
    print(f"  Fetching: {url}")
    try:
        html_text = curl_fetch(url)
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}")
        return None

    soup = BeautifulSoup(html_text, "lxml")

    # Extract title
    title = None
    # Try og:title first
    og_title = soup.find("meta", property="og:title")
    if og_title:
        title = og_title.get("content", "").strip()
    if not title:
        h1 = soup.find("h1")
        if h1:
            title = h1.get_text(strip=True)
    if not title:
        title_tag = soup.find("title")
        if title_tag:
            title = title_tag.get_text(strip=True).split("|")[0].strip()
    if not title:
        title = extract_slug_from_url(url).replace("-", " ").title()

    # Extract meta description
    description = ""
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc:
        description = meta_desc.get("content", "").strip()
    if not description:
        og_desc = soup.find("meta", property="og:description")
        if og_desc:
            description = og_desc.get("content", "").strip()

    # Extract categories and tags
    categories = []
    tags = []
    # Look for category/tag links
    for a in soup.find_all("a", rel="category tag"):
        categories.append(a.get_text(strip=True))
    for a in soup.find_all("a", rel="tag"):
        tag_text = a.get_text(strip=True)
        if tag_text not in categories:
            tags.append(tag_text)

    # Extract article content
    article_html = None

    # Try multiple selectors for content
    selectors = [
        ("article", {}),
        ("div", {"class": "entry-content"}),
        ("div", {"class": "post-content"}),
        ("div", {"class": "article-content"}),
        ("div", {"class": re.compile(r"content")}),
        ("main", {}),
    ]

    for tag, attrs in selectors:
        content_el = soup.find(tag, attrs)
        if content_el:
            # Remove navigation, comments, sharing buttons, etc.
            for unwanted in content_el.find_all(["nav", "footer", "aside"]):
                unwanted.decompose()
            for unwanted in content_el.find_all(class_=re.compile(
                r"(comment|share|social|related|sidebar|nav|menu|footer|subscribe|newsletter)"
            )):
                unwanted.decompose()
            # Remove script and style tags
            for unwanted in content_el.find_all(["script", "style", "noscript"]):
                unwanted.decompose()
            article_html = str(content_el)
            break

    if not article_html:
        print(f"  WARNING: Could not find article content for {url}")
        return None

    # Find all images in the article
    content_soup = BeautifulSoup(article_html, "lxml")
    img_urls = set()
    for img in content_soup.find_all("img"):
        src = img.get("src") or img.get("data-src") or ""
        if src and not src.startswith("data:"):
            # Make absolute URL
            if src.startswith("//"):
                src = "https:" + src
            elif src.startswith("/"):
                src = BASE_URL + src
            elif not src.startswith("http"):
                src = BASE_URL + "/" + src
            img_urls.add(src)
            # Update the img tag to use absolute URL for later rewriting
            img["src"] = src

    # Extract cover image (og:image or first image)
    cover_image = None
    og_image = soup.find("meta", property="og:image")
    if og_image:
        cover_url = og_image.get("content", "")
        if cover_url:
            img_urls.add(cover_url)
            cover_image = cover_url

    # Get date
    date = extract_date_from_url(url)
    if not date:
        # Try meta tags
        time_el = soup.find("time")
        if time_el and time_el.get("datetime"):
            date = time_el["datetime"]
        else:
            date = "2019-01-01T00:00:00Z"

    # Get slug
    slug = extract_slug_from_url(url)

    # Build URL path for alias
    parsed = urllib.parse.urlparse(url)
    url_path = parsed.path

    return {
        "title": title,
        "date": date,
        "slug": slug,
        "description": description,
        "categories": categories,
        "tags": tags,
        "article_html": str(content_soup),
        "img_urls": img_urls,
        "cover_image": cover_image,
        "url_path": url_path,
    }


def build_front_matter(article, cover_local=None):
    """Build Hugo front matter YAML."""
    # Escape quotes in title
    title = article["title"].replace('"', '\\"')
    lines = [
        "---",
        f'title: "{title}"',
        f'date: {article["date"]}',
        "draft: false",
    ]

    if article["description"]:
        desc = article["description"].replace('"', '\\"')
        lines.append(f'description: "{desc}"')

    if article["categories"]:
        cats = ", ".join(f'"{c}"' for c in article["categories"])
        lines.append(f"categories: [{cats}]")

    if article["tags"]:
        tag_list = ", ".join(f'"{t}"' for t in article["tags"])
        lines.append(f"tags: [{tag_list}]")

    if cover_local:
        lines.append("cover:")
        lines.append(f'  image: "{cover_local}"')
        alt = article["title"].replace('"', '\\"')
        lines.append(f'  alt: "{alt}"')

    # Add alias for original URL path
    if article["url_path"]:
        lines.append("aliases:")
        lines.append(f'  - "{article["url_path"]}"')

    lines.append("ShowToc: true")
    lines.append("TocOpen: false")
    lines.append("---")
    return "\n".join(lines)


def process_article(url):
    """Process a single article: extract, download images, save as Hugo content."""
    article = extract_article(url)
    if not article:
        return False

    slug = article["slug"]
    post_dir = CONTENT_DIR / slug
    post_dir.mkdir(parents=True, exist_ok=True)

    # Download images
    img_map = {}
    for img_url in article["img_urls"]:
        local_path = download_image(img_url, post_dir)
        if local_path:
            img_map[img_url] = local_path

    # Convert HTML to Markdown
    markdown_content = custom_md(
        article["article_html"],
        heading_style="ATX",
        bullets="-",
        strip=["script", "style", "noscript"],
    )

    # Rewrite image URLs to local paths
    markdown_content = rewrite_image_urls(markdown_content, img_map)

    # Also handle any remaining WordPress image URLs that might use different formats
    # e.g., URL-encoded versions or resized versions
    for remote_url, local_path in img_map.items():
        # Try URL-decoded version
        decoded = urllib.parse.unquote(remote_url)
        if decoded != remote_url:
            markdown_content = markdown_content.replace(decoded, local_path)
        # Try without query params
        no_query = remote_url.split("?")[0]
        if no_query != remote_url and no_query in markdown_content:
            markdown_content = markdown_content.replace(no_query, local_path)

    # Clean up the markdown
    # Remove excessive blank lines
    markdown_content = re.sub(r"\n{4,}", "\n\n\n", markdown_content)
    # Remove any remaining HTML comments
    markdown_content = re.sub(r"<!--.*?-->", "", markdown_content, flags=re.DOTALL)
    # Strip leading/trailing whitespace
    markdown_content = markdown_content.strip()

    # Determine cover image
    cover_local = None
    if article["cover_image"] and article["cover_image"] in img_map:
        cover_local = img_map[article["cover_image"]]

    # Build front matter
    front_matter = build_front_matter(article, cover_local)

    # Write the post
    post_file = post_dir / "index.md"
    with open(post_file, "w", encoding="utf-8") as f:
        f.write(front_matter)
        f.write("\n\n")
        f.write(markdown_content)
        f.write("\n")

    print(f"  Saved: {post_file} ({len(article['img_urls'])} images)")
    return True


def main():
    """Main entry point."""
    print("=" * 60)
    print("e4developer.com WordPress to Hugo Migration Scraper")
    print("=" * 60)

    # Create content directory
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    # Fetch sitemap
    urls = fetch_sitemap()

    # Filter URLs
    article_urls = [u for u in urls if not should_skip(u)]
    print(f"After filtering: {len(article_urls)} articles to process")

    # Process each article
    success = 0
    failed = 0
    for i, url in enumerate(article_urls, 1):
        print(f"\n[{i}/{len(article_urls)}] Processing...")
        try:
            if process_article(url):
                success += 1
            else:
                failed += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            failed += 1
        # Be polite - small delay between requests
        time.sleep(0.5)

    print(f"\n{'=' * 60}")
    print(f"Done! Processed {success} articles successfully, {failed} failed.")
    print(f"Content saved to: {CONTENT_DIR}")


if __name__ == "__main__":
    main()
