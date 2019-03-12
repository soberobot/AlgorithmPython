# -*- coding: utf-8 -*-
# 斐波那契数列


# 方法 1: 递归
def f(n):
  if n <= 0:
    return 0
  if n == 1:
    return 1
  return f(n - 1) + f(n - 2)


# 方法 2: 生成器
def fib(num):
  a, b = 0, 1
  for i in range(num):
    yield b
    a, b = b, a + b


# 方法 3: 循环
def fi(num):
  if num < 0:
    return 0
  elif num == 0:
    return [0]
  elif num == 1:
    return [0, 1]
  else:
    l = [0, 1]
    for i in list(range(num))[2:]:
        l.append(l[i - 1] + l[i - 2])
  return l


if __name__ == "__main__":
  print(f(0))
  print(f(1))
  print(f(9))
  print("____________")
  print(list(fib(0)))
  print(list(fib(1)))
  print(list(fib(9)))
  print("____________")
  print(fi(0))
  print(fi(1))
  print(fi(9))
