# -*- coding: utf-8 -*-
# 链表中倒数第 K 个节点


class Node(object):

  def __init__(self, val):
    self.val = val
    self.next = None


class ChainTable(object):

  def __init__(self, data):
    self.length = len(data)
    self.head = Node(data[0]) if self.length > 0 else None
    p = self.head
    for val in data[1:]:
      p.next = Node(val)
      p = p.next

  def kth_node_from_end(self, k):
    if not self.head:
      return None
    if k > self.length or k <= 0:
      return None
    p_ahead = self.head
    p_behind = self.head
    for i in range(k - 1):
      p_ahead = p_ahead.next
    while p_ahead.next:
      p_ahead = p_ahead.next
      p_behind = p_behind.next
    return p_behind.val


if __name__ == "__main__":
  ct = ChainTable([1, 2, 3, 4, 5, 6])
  print(ct.kth_node_from_end(0))
  print(ct.kth_node_from_end(1))
  print(ct.kth_node_from_end(2))
  print(ct.kth_node_from_end(3))
  print(ct.kth_node_from_end(4))
  print(ct.kth_node_from_end(5))
  print(ct.kth_node_from_end(6))
  print(ct.kth_node_from_end(7))
  print("-" * 9)
  ct2 = ChainTable([])
  print(ct.kth_node_from_end(2))
