# -*- coding: utf-8 -*-
# 二叉树的镜像


from collections import deque


class TreeNode(object):

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


class Tree(object):

  def __init__(self):
    self.root = None

  def construct_tree(self, values):
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


def mirror(root):
  if root:
    root.left, root.right = root.right, root.left
    mirror(root.right)
    mirror(root.left)


if __name__ == "__main__":
  tree = Tree()
  tree.construct_tree([1, 2, 3, 4, 5, 6, 7, 8])
  print(tree.bfs())
  mirror(tree.root)
  print(tree.bfs())


