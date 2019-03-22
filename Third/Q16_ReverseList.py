# -*- coding: utf-8 -*-
# 反转链表


class Node(object):

  def __init__(self, val):
    self.val = val
    self.next = None


class LinkList(object):

  def __init__(self, data):
    self.length = len(data)
    self.head = Node(data[0]) if self.length > 0 else None
    p = self.head
    for val in data[1:]:
      p.next = Node(val)
      p = p.next

  def reverse_list(self):
    if not self.head or not self.head.next:
      return self.head
    p_ahead = None
    p = self.head
    p_behind = p.next
    while p.next:
      p.next = p_ahead  # 反转
      # 所有指针向后走一步
      p_ahead = p
      p = p_behind
      p_behind = p.next
    p.next = p_ahead
    self.head = p
    return self.head.val


def print_link_list(head):
  p = head
  while p:
    print("node value: ", p.val)
    p = p.next


if __name__ == "__main__":
  data = [1, 2, 3, 4, 5]
  ct = LinkList(data)
  print_link_list(ct.head)
  print("-" * 8)
  print("new_head: ", ct.reverse_list())
  print("-" * 8)
  print_link_list(ct.head)
