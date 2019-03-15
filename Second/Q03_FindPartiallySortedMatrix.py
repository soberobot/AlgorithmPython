# -*- coding: utf-8 -*-
# 二维数组的查找


def find(target, arr):
  if not arr:
    return False
  rows, cols = len(arr), len(arr[0])
  row, col = 0, cols-1
  while col >= 0 and row <= rows-1:
    if arr[row][col] == target:
      return True
    elif arr[row][col] > target:
      col -= 1
    elif arr[row][col] < target:
      row += 1


if __name__ == "__main__":
  matrix = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
  num = 7
  print(find(num, matrix))
