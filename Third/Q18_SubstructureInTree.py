# -*- coding: utf-8 -*-
# 树的子结构

from collections import deque


class TreeNode(object):

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


class Tree(object):

  def __init__(self):
    self.root = None

  def construct_tree(self, values=None):
    if not values:
      return None
    self.root = TreeNode(values[0])
    queue = deque([self.root])
    leng = len(values)
    idx = 1
    while idx < leng:
      node = queue.popleft()
      if node:
        node.left = TreeNode(values[idx])
        queue.append(node.left)
        if idx + 1 < leng:
          node.right = TreeNode(values[idx + 1])
          queue.append(node.right)
          idx += 1
        idx += 1

  def bfs(self):
    ret = []
    queue = deque([self.root])
    while queue:
      node = queue.popleft()
      if node:
        ret.append(node.val)
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
    return ret


def sub_tree(tree1, tree2):
  """

  Args:
    tree1: bigger tree.
    tree2: smaller tree.
  """
  if tree1 and tree2:
    if tree1.val == tree2.val:
      return sub_tree(tree1.left, tree2.left) and sub_tree(tree1.right,
                                                           tree2.right)
    else:
      return sub_tree(tree1.left, tree2) or sub_tree(tree1.right, tree2)

  if not tree1 and tree2:  # 1 到终点了 2 还有
    return False

  return True  # 2 到终点了 1 还有，或者同时都到尽头了


if __name__ == "__main__":
  tree1 = Tree()
  tree1.construct_tree([6, 5, 4, 3, 2, 1, 0])
  print(tree1.bfs())
  tree2 = Tree()
  tree2.construct_tree([4, 1, 0])
  print(tree2.bfs())
  print("is sub_tree: ", sub_tree(tree1.root, tree2.root))
