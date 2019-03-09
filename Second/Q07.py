# -*- coding: utf-8 -*-
# 用两个栈实现队列
# 队列：只允许在表的前端（front）进行删除操作，而在表的后端（rear）进行插入操作
# 堆栈：仅允许在表的一端进行插入和删除运算
# 也就是说用 python 的列表模拟队列，只能用 append 和 pop 方法


class MyQueue(object):

  def __init__(self, data):
    self.stack1 = data
    self.stack2 = []

  def push(self, val):
    self.stack1.append(val)

  def pop(self):
    if self.stack2:
      return self.stack2.pop()

    while self.stack1:
      self.stack2.append(self.stack1.pop())

    ele = self.stack2.pop()

    while self.stack2:
      self.stack1.append(self.stack2.pop())

    return ele if self.stack1 else "Empty Queue"


if __name__ == "__main__":
  q = MyQueue([1, 2, 3, 4, 5])
  q.push(6)
  print(q.stack1)
  q.push(7)
  print(q.stack1)
  q.pop()
  print(q.stack1)
  q.push(11)
  print(q.stack1)
  q.pop()
  print(q.stack1)
  q.push(22)
  print(q.stack1)
  q.pop()
  print(q.stack1)
  q.pop()
  print(q.stack1)
  q.pop()
  print(q.stack1)
