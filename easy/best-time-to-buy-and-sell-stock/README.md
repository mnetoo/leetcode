# Best Time to Buy and Sell Stock

## Problem
Given an array `prices` where `prices[i]` represents the price of a stock on day `i`, determine the maximum profit that can be achieved by buying one stock and selling it later.

You may only complete **one transaction**.



# Solution Idea
The solution keeps track of:

* The minimum stock price found so far
* The maximum profit achievable at each step

For every price:

1. Calculate the profit if selling on the current day
2. Update the maximum profit if necessary
3. Update the minimum price if a smaller value is found

This avoids checking all possible pairs and achieves linear complexity.


## Time Complexity
```text id="o2kt2v"
O(n)
```

The array is traversed only once.
## Space Complexity
```text id="2o4z4e"
O(1)
```
Only constant extra memory is used.


# Concepts Used
* Arrays
* Greedy approach
* Single-pass optimization
* Maximum subproblem tracking