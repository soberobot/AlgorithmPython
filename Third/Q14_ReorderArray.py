# -*- coding: utf-8 -*-
# 调整数组顺序使奇数位于偶数前面


def reorder(data, func):
  p0 = 0
  p1 = len(data) - 1
  while p0 < p1:
    while not func(data[p0]):
      p0 = p0 + 1
    while func(data[p1]):
      p1 = p1 - 1
    if p0 < p1:
      data[p0], data[p1] = data[p1], data[p0]


def is_odd(num):
  if num % 2 is 0:
    return True
  else:
    return False


if __name__ == "__main__":
  data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  reorder(data, is_odd)
  print(data)
