# -*- coding: utf-8 -*-
# 包含 min 函数的栈


class Stack(object):

  def __init__(self):
    self.data = []
    self.mins = []

  def push(self, num):
    self.data.append(num)
    if not self.mins:
      self.mins.append(num)
    else:
      if self.mins and self.mins[-1] < num:
        self.mins.append(self.mins[-1])
      else:
        self.mins.append(num)

  def pop(self):
    if self.data:
      self.mins.pop()
      return self.data.pop()
    return None

  def min(self):
    print(self.mins[-1] if self.mins else None)
    return self.mins[-1] if self.mins else None

  def print(self):
    print(self.data)
    print("mins: ", self.mins)
    print("-----")


if __name__ == "__main__":
  s = Stack()
  s.push(3)
  s.min()
  s.print()
  s.push(9)
  s.min()
  s.print()
  s.push(1)
  s.min()
  s.print()
  s.pop()
  s.min()
  s.print()
  s.pop()
  s.min()
  s.print()
  s.pop()
  s.min()
  s.print()
  s.push(2)
  s.min()
  s.print()
