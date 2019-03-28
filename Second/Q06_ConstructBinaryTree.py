# -*- coding: utf-8 -*-
# 重建二叉树


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

  def preorder(self):
    ret = []

    def traversal(node):
      if not node:
        return
      ret.append(node.val)
      traversal(node.left)
      traversal(node.right)

    traversal(self.root)
    return ret

  def inorder(self):
    ret = []

    def traversal(node):
      if not node:
        return
      traversal(node.left)
      ret.append(node.val)
      traversal(node.right)

    traversal(self.root)
    return ret
  
  def in_order_traverse(self, root):
    """另一种中序遍历"""

    if not root:
      return
    self.in_order_traverse(root.left)
    print(root.val)
    self.in_order_traverse(root.right)

  def postorder(self):
    ret = []

    def traversal(node):
      if not node:
        return
      traversal(node.left)
      traversal(node.right)
      ret.append(node.val)

    traversal(self.root)
    return ret


def rebuild_tree(preorder=None, inorder=None):
  """

  Args:
    preorder(list):
    inorder(list):

  Returns:

  """
  if not preorder or not inorder:
    return None
  idx = inorder.index(preorder[0])
  left = inorder[:idx]
  right = inorder[idx + 1:]
  root = TreeNode(inorder[idx])
  root.left = rebuild_tree(preorder[1:len(left) + 1], left)
  root.right = rebuild_tree(preorder[-len(right):], right)
  return root


if __name__ == "__main__":
  tree = Tree()
  tree.construct_tree([1, 2, 3, 4, 5, 6, 7, 8])
  print(tree.preorder())
  print(tree.inorder())
  print(tree.postorder())
  print("-" * 8)
  root = rebuild_tree(tree.preorder(), tree.inorder())
  tree.root = root
  print(tree.bfs())
  print(tree.preorder())
  print(tree.inorder())
  print(tree.postorder())
