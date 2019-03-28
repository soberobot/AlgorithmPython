# -*- coding: utf-8 -*-
# 从上往下打印二叉树


from collections import deque


class TreeNode(object):

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


class Tree(object):

  def __init__(self):
    self.root = None

  def constract(self, values):
    if not values:
      return
    self.root = TreeNode(values[0])
    queue = deque([self.root])
    leng = len(values)
    idx = 1
    while idx < leng:
      node = queue.popleft()
      if node:
        node.left = TreeNode(values[idx])
        queue.append(node.left)
        if idx < leng:
          node.right = TreeNode(values[idx + 1])
          queue.append(node.right)
          idx += 1
        idx += 1

  def print_tree(self):
    queue = deque([self.root])
    while queue:
      node = queue.popleft()
      if node:
        print(node.val)
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)


if __name__ == "__main__":
  tree = Tree()
  tree.constract([1, 2, 3, 4, 5, 6, 7, 8, 9])
  tree.print_tree()
