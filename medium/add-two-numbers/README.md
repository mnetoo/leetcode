# Add Two Numbers

## Problem
Two non-empty linked lists represent two non-negative integers.

The digits are stored in reverse order, where each node contains a single digit.

The goal is to add the two numbers and return the result as a linked list.


# Example
```text id="t9v44j"
Input:
l1 = [2,4,3]
l2 = [5,6,4]

Output:
[7,0,8]
```

Explanation:
```text id="s8a8u4"
342 + 465 = 807
```


# Solution Idea

This solution follows three main steps:
1. Convert both linked lists into arrays
2. Reconstruct the integer values represented by the lists
3. Sum the numbers and rebuild the resulting linked list

Because the digits are stored in reverse order, each position represents a power of 10.

Example:
```text id="n8hy3n"
[2,4,3] → 342
```

The reconstruction works as:
```text id="qex8i8"
2 × 10⁰
4 × 10¹
3 × 10²
```
After calculating the sum, the algorithm creates a new linked list digit by digit.

## Time Complexity
```text id="dcfym9"
O(n + m)
```
Where:
* `n` is the size of the first list
* `m` is the size of the second list
The lists are traversed linearly.

## Space Complexity
```text id="w5cjlwm"
O(n + m)
```
Extra arrays are used to store the digits temporarily.

# Concepts Used
* Linked Lists
* Integer reconstruction
* Digit manipulation
* List traversal
* Modular arithmetic