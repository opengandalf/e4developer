---
title: "Implementing Minimax Algorithm in Java"
date: 2018-09-23T00:00:00Z
draft: false
description: "If you want to write a program that is able to play a strategy game, there are good chances that you will be looking at a Minimax algorithm."
categories: ["Algorithms", "Java"]
cover:
  image: "images/minimax-java.jpg"
  alt: "Implementing Minimax Algorithm in Java"
aliases:
  - "/2018/09/23/implementing-minimax-algorithm-in-java/"
  - "/implementing-minimax-algorithm-in-java/"
ShowToc: true
TocOpen: false
---If you want to write a program that is able to play a strategy game, there are good chances that you will be looking at a Minimax algorithm. This is especially true when it comes to games like chess, where variations of the Minimax algorithm are what is used to build the strongest chess-playing programs in existence. In this article, I will look at implementing the basic version of the Minimax algorithm with Java.

## Minimax Algorithm – a quick introduction

Minimax is a simple algorithm that tells you which move to play in a game. A detailed explanation is [available on Wikipedia](https://en.wikipedia.org/wiki/Minimax), but here is my quick, less rigorous outline:

- Take a game where you and your opponent take alternate turns
- Each time you take a turn you choose the best possible move (max)
- Each time your opponent takes a turn, the worst move for you is chosen (min), as it benefits your opponent the most
- Looking forward and using these assumptions- which moves leads you to victory?

Minimax is basically doing what I described above, but with a simple algorithm. In this article, I will implement the most basic version of Minimax where I omit the two possible improvements:

- I will look forward through the entire game tree, finding the optimal strategy (impossible in more complicated games).
- I will not use any pruning of branches (inefficient in practical, non-trivial scenarios).

Stopping rules and pruning can be added in the future when I use the algorithm to play chess or work with another non-trivial game.

## Implementing Minimax with Java

Based on the pseudocode in [“Artifical Intelligence: The Modern Approach” (Amazon)](https://amzn.to/2Js9Eb6), I have decided to implement the template for the algorithm. Written in Java, it can look like this:

```

public final class MinimaxTemplate {

    private MinimaxTemplate() {}

    public static State minimaxDecision(State state) {
        return state.getActions().stream()
                .max(Comparator.comparing(MinimaxTemplate::minValue)).get();
    }

    private static double maxValue(State state) {
        if(state.isTerminal()){
            return state.getUtility();
        }
        return state.getActions().stream()
                .map(MinimaxTemplate::minValue)
                .max(Comparator.comparing(Double::valueOf)).get();
    }

    private static double minValue(State state) {
        if(state.isTerminal()){
            return state.getUtility();
        }
        return state.getActions().stream()
                .map(MinimaxTemplate::maxValue)
                .min(Comparator.comparing(Double::valueOf)).get();
    }

    //State Class
}

```

You can call *minimaxDecision*with a *State* object representing the current state of the game.

To get a usable implementation of Minimax you need to implement this *State* object template:

```

public static class State {

    public State(){
        //create a state
    }

    Collection<State> getActions(){
        List<State> actions = new LinkedList<>();
        //generate actions
        return actions;
    }

    boolean isTerminal() {
        //add some logic
        return false;
    }

    double getUtility() {
        //add some logic
        return 0;
    }
}

```

## Solving a simple game with Minimax

While reading different articles on the subject I found[Introduction to Minimax Algorithm by Baeldung](https://www.baeldung.com/java-minimax-algorithm) which had a simple game described. This game inspired me to create something very similar:

- You start with the number
- Two players can reduce this number by the value 3, 4 or 5
- The number can’t go down below 0
- A player that can’t make a move loses

The Baeldung article uses Nodes explicitly while I just fill in my template coming up with the Class:

```

import java.util.*;

public final class Minimax {

    private Minimax() {}

    public static State minimaxDecision(State state) {
        return state.getActions().stream()
                .max(Comparator.comparing(Minimax::minValue)).get();
    }

    private static double maxValue(State state) {
        if(state.isTerminal()){
            return state.getUtility();
        }
        return state.getActions().stream()
                .map(Minimax::minValue)
                .max(Comparator.comparing(Double::valueOf)).get();
    }

    private static double minValue(State state) {
        if(state.isTerminal()){
            return state.getUtility();
        }
        return state.getActions().stream()
                .map(Minimax::maxValue)
                .min(Comparator.comparing(Double::valueOf)).get();
    }

    public static class State {

        final int state;
        final boolean firstPlayer;
        final boolean secondPlayer;

        public State(int state, boolean firstPlayer){
            this.state = state;
            this.firstPlayer = firstPlayer;
            this.secondPlayer = !firstPlayer;
        }

        Collection<State> getActions(){
            List<State> actions = new LinkedList<>();
            if(state > 4){
                actions.add(new State(state-5, secondPlayer));
            }
            if(state > 3){
                actions.add(new State(state-4, secondPlayer));
            }
            if(state > 2){
                actions.add(new State(state-3, secondPlayer));
            }
            return actions;
        }

        boolean isTerminal() {
            return state < 3;
        }

        double getUtility() {
            if(firstPlayer)
                return -1;
            else
                return 1;
        }
    }
}

```

That can be run by a Main class as follows:

```

public class Main {

    public static void main(String[] args){
        System.out.println("Welcome to my minimax algorithm");
        boolean end = false;
        int val = 21;
        boolean first = true;
        while(!end) {
            System.out.println("Current position = "+ val +", Player one: " + first);
            Minimax.State s = new Minimax.State(val, true);
            Minimax.State decision = Minimax.minimaxDecision(s);
            val = decision.state;
            if(decision.isTerminal()){
                end = true;
                System.out.println("Current position = "+ val +", Player one won: " + first);
                System.out.println("Game over");
            }
            first =! first;
        }
    }
}

```

This algorithm perfectly solves this simple game.

## What next?

It is fun to use Minimax to solve simple games. In order to tackle something more serious there are three key improvements to be made:

- We should be able to evaluate game state before win-lose is decided. For example in chess- having more pieces usually means advantage etc.
- We need to be able to search only to a predetermined depth (this should be easy already with the template given).
- I need to look at Alpha-Beta Pruning algorithm to improve the performance
- Having an object representing the state is potentially slow, but this can be looked at last.

## Summary

A future part of this article is pretty much guaranteed as I still have quite a way to go on my quest for writing a semi-advanced game playing program.

I hope this was interesting and made you want to try to play with Minimax yourself. Good luck!
