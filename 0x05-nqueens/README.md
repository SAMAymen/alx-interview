# 0x05. N Queens
## Task Summary

The N queens puzzle involves placing N non-attacking queens on an N×N chessboard. Write a program `nqueens` that solves this problem, ensuring N is an integer ≥ 4. If the input is invalid, the program should print appropriate error messages and exit with status 1. The program should output all possible solutions, one per line, without a specific order, and only the `sys` module is allowed for import.

## Example

```
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```
