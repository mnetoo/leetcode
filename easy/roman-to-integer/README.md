# Roman to Integer

## Problem
Roman numerals are represented using combinations of symbols:
| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

The objective is to convert a Roman numeral string into its integer representation.
Roman numerals also contain subtraction rules, such as:

| Combination | Value |
| ----------- | ----- |
| IV          | 4     |
| IX          | 9     |
| XL          | 40    |
| XC          | 90    |
| CD          | 400   |
| CM          | 900   |

# Solution Idea
The solution traverses the string from left to right.
For each symbol:
* Compare its value with the next symbol
* If the current value is smaller than the next one, subtract it
* Otherwise, add it normally
This works because subtraction in Roman numerals only happens when a smaller symbol appears before a larger valid symbol.

## Time Complexity
```text id="yz3czu"
O(n)
```
The algorithm traverses the string only once.

## Space Complexity
```text id="2u0bmr"
O(1)
```
Only constant extra memory is used.

# Concepts Used
* String traversal
* Symbol mapping
* Conditional logic
* Greedy decision making