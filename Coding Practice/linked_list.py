__author__ = 'pratik'

class Node:
  def __init__(self, value):
    self.data = value
    self.next = None



class LinkedList:
  def __init__(self, first=None):
    self.first = first

  def add(self, node):
    if not self.first:
      self.first = node
      return self.first

    prev = None
    next = self.first
    while(next):
      prev = next
      next = prev.next

    prev.next = node
    return self.first

  def get_first(self):
    return self.first

  def traverse(self):
    current = self.first
    while(current):
      current = current.next









if __name__ == '__main__':
  ll = LinkedList()
  for i in range(0, 10):
    print i
    y = Node(i)
    first = ll.add(y)
    ll.traverse()