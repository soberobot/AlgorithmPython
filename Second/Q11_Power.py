# -*- coding: utf-8 -*-
# 数值的整数次方


def pow(base, exp):
  if base is 0:
    if exp <= 0:
      return '无意义'
    else:
      return 0
  else:
    if exp is 0:
      return 1
    elif exp > 0:
      return pow_posi_exp(base, exp)
    else:
      return 1 / pow_posi_exp(base, -exp)


def pow_posi_exp(base, exp):
  # if exp % 2 is 1:
  #   return pow_posi_exp(base, exp - 1) * pow_posi_exp(base, exp - 1) * base
  # else:
  #   return pow_posi_exp(base, exp - 1) * pow_posi_exp(base, exp - 1)
  j = 1
  for i in range(exp):
    j *= base
  return j


if __name__ == "__main__":
  print(pow(-2, -3))
  print(pow(-2, 0))
  print(pow(-2, 3))
  print("----------")
  print(pow(0, -2))  # 无意义
  print(pow(0, 0))  # 无意义
  print(pow(0, 2))
  print("----------")
  print(pow(2, -3))
  print(pow(2, 0))
  print(pow(2, 3))
