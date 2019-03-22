# -*- coding: utf-8 -*-
# 合并两个排序的链表


class Node(object):

  def __init__(self, val):
    self.val = val
    self.next = None


class LinkList(object):

  def __init__(self, data):
    self.head = Node(data[0]) if len(data) > 0 else None
    p = self.head
    for val in data[1:]:
      p.next = Node(val)
      p = p.next


def merge_lists(head1, head2):
  if not head1:
    return head2
  if not head2:
    return head1

  if head1.val < head2.val:
    merge_head = head1
    merge_head.next = merge_lists(head1.next, head2)
  else:
    merge_head = head2
    merge_head.next = merge_lists(head1, head2.next)
  return merge_head


def print_link_list(head):
  p = head
  while p:
    print("node value: ", p.val)
    p = p.next


if __name__ == "__main__":
  link_list_1 = LinkList([1, 3, 5, 7, 9])
  print("-" * 8)
  link_list_2 = LinkList([2, 4, 6, 8, 10])
  print_link_list(link_list_1.head)
  print_link_list(link_list_2.head)
  merge_list = merge_lists(link_list_1.head, link_list_2.head)
  print("-" * 8)
  print_link_list(merge_list)
