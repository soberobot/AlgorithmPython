# -*- coding: utf-8 -*-
# 二叉树中和为某一值的路径


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


def find_path(root, target):
  ret = []
  if not root:
    return ret

  path = [root]
  sums = [root.val]

  def dfs(node):
    if node.left:
      path.append(node.left)
      sums.append(sums[-1] + node.left.val)
      dfs(node.left)
    if node.right:
      path.append(node.right)
      sums.append(sums[-1] + node.right.val)
      dfs(node.right)
    if not node.left and not node.right:
      if sums[-1] == target:
        ret.append([i.val for i in path])
    path.pop()
    sums.pop()

  dfs(root)
  return ret


if __name__ == "__main__":
  tree = Tree()
  tree.construct_tree([10, 5, 12, 4, 7])
  print(tree.bfs())
  print(find_path(tree.root, 22))
