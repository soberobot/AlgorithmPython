# -*- coding: utf-8 -*-
#
# 打印 1 到最大的 n 位数
# python 支持大数计算，无限位数。
# 对于小整数，它会使用机器自身的整数计算功能去快速计算，当超出机器自身所能支持的范围的时候，自动转换大数计算。


# 方法 1
def print_max_n(n):
  if n <= 0:
    return
  for i in range(10 ** n):
    print(i)

# 方法 2: n 个从 0 到 9 的全排列


if __name__ == "__main__":
  print_max_n(1)
