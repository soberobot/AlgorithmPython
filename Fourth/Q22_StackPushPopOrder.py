# -*- coding: utf-8 -*-
# 栈的压入弹出序列


from collections import deque


def stack_order(list0, list1):
  """
  Args:
    list0: 压入序列
    list1: 弹出序列
  """

  stack = deque([])
  stack.append(list0.popleft())
  while list1:
    while list0:
      if stack[-1] != list1[0]:
        stack.append(list0.popleft())
      else:
        list1.popleft()
        stack.pop()
    if stack.pop() != list1.popleft():
      return False
  return True


if __name__ == "__main__":
  list0 = deque([1, 2, 3, 4, 5])
  list1 = deque([4, 5, 3, 2, 1])
  print(stack_order(list0, list1))
  list0 = deque([1, 2, 3, 4, 5])
  list1 = deque([4, 3, 5, 1, 2])
  print(stack_order(list0, list1))
  list0 = deque([1, 2, 3])
  list1 = deque([2, 3, 1])
  print(stack_order(list0, list1))
