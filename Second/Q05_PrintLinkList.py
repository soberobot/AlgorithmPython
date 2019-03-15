# -*- coding: utf-8 -*-
# 从头到尾打印单链表


class Node(object):

  def __init__(self, val):
    self.val = val
    self.next = None


class ChainTable(object):

  def __init__(self, data):
    self.head = Node(data[0])
    p = self.head
    for val in data[1:]:
      p.next = Node(val)
      p = p.next


# 方法 1: 递归
def print_chain_table(pointer):
  if pointer:
    print(pointer.val)
    print_chain_table(pointer.next)


# 方法 2: 常规
def print_link_list(pointer):
  while pointer:
    print(pointer.val)
    pointer = pointer.next


if __name__ == "__main__":
  ct = ChainTable([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
  print_chain_table(ct.head)
  print_link_list(ct.head)
