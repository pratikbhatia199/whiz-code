__author__ = 'pratik'
class Node:
  def __init__(self, data=0, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self, first=None):
    self.first = first

  def insert(self, node):
    if not self.first:
      self.first = node
      return self.first

    current = self.first
    previous = None
    while(current.next and current.data < node.data):
      previous = current
      current = current.next

    


