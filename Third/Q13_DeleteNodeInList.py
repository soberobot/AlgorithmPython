# -*- coding: utf-8 -*-
# 在O(1)时间删除链表结点


class Node(object):

  def __init__(self, value):
    self.val = value
    self.next = None


class LinkList(object):

  def __init__(self, data):
    self.head = Node(data[0])
    p = self.head
    for i in data[1:]:
      p.next = Node(i)
      p = p.next


def print_chain_table(pointer):
  if pointer:
    print(pointer.val)
    print_chain_table(pointer.next)


def del_node(ll, node):
  if ll.head == node:
    del node
    ll.head = None
  if node.next is None:
    p = ll.head
    while p:
      if p.next == node:
        p.next = None
      p = p.next
  else:
    node.val = node.next.val
    n = node.next
    node.next = n.next
    del n


if __name__ == "__main__":
  ct = LinkList([0, 1, 2, 3, 4])
  print_chain_table(ct.head)
