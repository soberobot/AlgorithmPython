# -*- coding: utf-8 -*-
# 旋转数组的最小数字

import math


def find_min(data):
  p1 = 0
  p2 = len(data) - 1
  if data[p1] < data[p2]:
    return data[0]

  while p2 - p1 != 1:
    p = math.ceil((p2 + p1) / 2)
    if data[p] < data[p1]:
      p2 = p
    if data[p] > data[p2]:
      p1 = p
    if data[p] == data[p1] == data[p2]:
      return min(data)
  return data[p2]


if __name__ == "__main__":
  print(1, find_min([2, 3, 0, 0, 0]))
  print(2, find_min([1, 0, 0, 0, 1]))
  print(3, find_min([3, 4, 5, 1, 2]))
  print(4, find_min([5, 5, 5, 3, 4]))
  print(5, find_min([1, 1, 1, 0, 1]))
  print(6, find_min([1, 0, 1, 1, 1]))
