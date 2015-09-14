__author__ = 'pratik'

class Node:
  def __init__(self, next=None, data=0):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self, first=None):
    self.first = first

  def insert(self, node):
    if not self.first:
      self.first = node
      return self.first

    previous = None
    current = self.first
    while( current!=None and current.data < node.data):
      previous = current
      current = current.next

    if not previous:
      node.next = self.first
      self.first = node
      return self.first

    node.next = previous.next
    previous.next = node

    return self.first

  def traverse(self):
    current = self.first
    while current!= None:
      print "data: ", current.data
      current = current.next


if __name__ == '__main__':
  list_inserts = [6,3,7,2, 9, -1]
  ll = LinkedList()
  node = Node(data=1)
  ll.traverse()
  ll.insert(node)
  ll.traverse()
  for value in list_inserts:
    node = Node(data=value)
    ll.insert(node)
  ll.traverse()

