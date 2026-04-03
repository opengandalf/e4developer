# e4developer.com Migration Spec

## Goal
Migrate the WordPress blog at e4developer.com to a Hugo static site on GitHub Pages.
The site should look modern, minimal, and techy — think dark mode, clean typography, subtle AI/tech vibes.

## Source
- WordPress site: https://www.e4developer.com
- Sitemap: https://www.e4developer.com/sitemap-1.xml
- ~95 articles from 2018-2020
- Topics: Microservices, Java, Spring Boot/Cloud, AWS, DevOps, tech leadership, software architecture
- Author: Bartosz Jedrzejewski

## Architecture
- **Static site generator:** Hugo
- **Theme:** Custom or PaperMod with heavy customization
- **Hosting:** GitHub Pages (repo: opengandalf/e4developer)
- **Domain:** e4developer.com (will be configured later)

## Design Requirements
- **Dark mode default** with light mode toggle
- **Minimal, techy aesthetic** — think Vercel/Stripe blog vibes
- Clean sans-serif typography (Inter or similar)
- Subtle tech accents — maybe a gradient or glow effect on headers
- Good code syntax highlighting (essential for a dev blog)
- Fast, no bloat, high Lighthouse score
- Mobile responsive
- Table of contents on longer posts
- Tags and categories preserved from WordPress
- Search (client-side lunr.js or similar)
- About page with author bio
- Social links (Twitter @e4developer, GitHub bjedrzejewski, LinkedIn)

## Migration Steps

### Phase 1: Scrape all content
1. Parse sitemap-1.xml to get all article URLs (skip /log-in/, /sign-up/, /reset-password/, /account/, /my-profile/, /member-directory/)
2. For each article URL, fetch the page and extract:
   - Title
   - Date (from URL path: /YYYY/MM/DD/slug/)
   - Full article content (HTML body)
   - All images (download to local)
   - Categories and tags if available
   - Meta description if available
3. Convert HTML content to clean Markdown
4. Save each article as Hugo content: content/posts/SLUG/index.md with front matter
5. Save images in each post's directory: content/posts/SLUG/images/

### Phase 2: Build Hugo site
1. Set up Hugo project structure
2. Configure hugo.toml with site metadata
3. Set up theme (PaperMod customized or custom theme)
4. Create layouts: home, single post, list, tags, categories, about
5. Add custom CSS for the techy/minimal look
6. Configure syntax highlighting
7. Add GitHub Actions workflow for auto-deploy to Pages

### Phase 3: Deploy
1. Push to GitHub
2. Enable GitHub Pages on the repo
3. Set up GitHub Actions workflow (.github/workflows/hugo.yml)

## Content Front Matter Format
```yaml
---
title: "Article Title"
date: 2018-01-13T00:00:00Z
draft: false
categories: ["Microservices", "Java"]
tags: ["spring-boot", "docker"]
description: "Brief description"
cover:
  image: "images/cover.jpg"  # if available
  alt: "Cover image description"
ShowToc: true
TocOpen: false
---
```

## Important Notes
- Preserve all original URLs as aliases for SEO
- Keep original publish dates
- Download ALL images — don't link to WordPress hosted ones
- The /start-here/ and /contact/ pages should become standalone pages
- Skip login/signup/account pages (WordPress-only)
- Code blocks should use proper language tags for syntax highlighting
- No AI-generated content — this is a straight migration of existing articles
