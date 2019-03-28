# -*- coding: utf-8 -*-
# 二叉搜索树的后序遍历序列


def is_post_order(values):
  if not values:
    return

  # 假设 None 列表可视为空树的后续遍历序列
  # 直到最后传入空数组说明遍历完且都符合条件
  if len(values) == 0:
    return True

  root = values[-1]
  leng = len(values)
  idx = 0
  while values[idx] < root:
    idx += 1
  right_idx = idx
  while idx < leng - 1:
    if values[idx] <= root:
      return False
    idx += 1

  left_ret = is_post_order(values[:right_idx])
  right_ret = is_post_order(values[right_idx: -1])
  return left_ret and right_ret


if __name__ == "__main__":
  values1 = [5, 7, 6, 9, 11, 10, 8]
  values2 = [7, 6, 5, 5]
  print(is_post_order(values1))
  print(is_post_order(values2))
