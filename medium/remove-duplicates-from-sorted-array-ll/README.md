# Remove Duplicates from Sorted Array II

## Problem
Given a sorted integer array `nums`, remove duplicates in-place such that each unique element appears **at most twice**.

The relative order of the elements must remain the same.

The function should return `k`, representing the number of valid elements remaining in the array.

The first `k` elements of `nums` should contain the final result.


# Example
## Input
```text id="3b9r3v"
nums = [1,1,1,2,2,3]
```
## Output
```text id="fjlwm4"
k = 5
nums = [1,1,2,2,3,_]
```

# Solution Idea
Since the array is already sorted, duplicates always appear consecutively.
The strategy is:
* Always allow the first two occurrences of a number
* Reject any occurrence that would create a third duplicate

To do this efficiently:
* Use a pointer `k` to track where the next valid element should be placed
* Compare the current value with the element at position `k - 2`
Why `k - 2`?

Because if the current value equals `nums[k - 2]`, it means we already stored two identical values.
Adding another one would violate the rule.


## Time Complexity
```text id="yfq3m8"
O(n)
```
The array is traversed only once.

## Space Complexity
```text id="cmjv7k"
O(1)
```
The algorithm modifies the array in-place without using extra memory.

# Concepts Used
* Two pointers
* In-place array modification
* Sorted array properties
* Duplicate filtering
* Linear traversal