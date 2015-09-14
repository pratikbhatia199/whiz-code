__author__ = 'pratik'

from collections import deque
from copy import copy

class Node:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right


class BinaryTree:
  def __init__(self, root=None):
    self.root = root
    self.queue = deque()
    self.set_visited = set()

  def inorder_traversal(self, root):
    if not root:
      return

    self.inorder_traversal(root.left)
    print "root data: ", root.data
    self.inorder_traversal(root.right)


  def insert(self, root, node):
    if self.root:
      print "root", self.root.data
    else:
      print "none", self.root

    if not root:
      self.root = node
      return self.root, node

    if root.data < node.data:
      if not root.right:
        root.right = node
        return root, node
      else:
        self.insert(root.right, node)

    if root.data > node.data:
      if not root.left:
        root.left = node
        return root, node
      else:
        self.insert(root.left, node)


    if root.data == node.data:
      if not root.left:
        root.left = node
        return root, node
      else:
        self.insert(root.left, node)

  def bfs_for_bst(self, queue):
    if len(queue) == 0:
      return
    current = queue.popleft()

    if current.left:
      queue.append(current.left)

    if current.right:
      queue.append(current.right)

    self.bfs_for_bst(queue)

  # def depth_first_search_for_bst(self):
  #   print "Doing depth first search".

  def lca(self, left_node, right_node, current_node):
    left = None
    right = None

    if current_node:
      if current_node == left_node:
        left = self.lca(left_node, right_node)
      if current_node == right_node:
        right = self.lca(left_node, right_node)

    if left and right:
      return current_node

    if left:
      return left

    if right:
      return right



  def is_balanced(self, node):
    if node == None:
      return 0
    left_height = self.is_balanced(node.left)
    right_height = self.is_balanced(node.right)
    if left_height == -1 or right_height == -1:
      return -1
    if abs(left_height - right_height) > 1:
      return -1
    else:
      return max(left_height+1, right_height+1)

  def root_to_leaf_path(self, list_path, root, current_path):
    print "inside root to leaf path"
    print "root", root.data


    current_path.append(root.data)
    print "current path", current_path

    if not root.left and not root.right:
      list_path.append(current_path)
      return list_path

    if root.left and root.right:
      copy_current_path = copy(current_path)
      list_path = self.root_to_leaf_path(list_path, root.left, current_path)
      return self.root_to_leaf_path(list_path, root.right, copy_current_path)x

    if root.left:
      return self.root_to_leaf_path(list_path, root.left, current_path)

    if root.right:
      return self.root_to_leaf_path(list_path, root.right, current_path)



if __name__ == '__main__':
  tree = BinaryTree()
  list_values = [3, 5, 1, 6, 2, 0, 8, 7, 4]
  for value in list_values:
    x = Node(value)
    returns = tree.insert(tree.root, x)
    if returns:
      for val in returns:
        if val:
          print val.data


  tree.inorder_traversal(tree.root)
  queue = deque()
  queue.append(tree.root)
  tree.bfs_for_bst(queue)
  print "Is balanced"
  balanced_tree = BinaryTree()
  list_new_values = [5, 3, 6, 2,  4, 7, 1 ]

      #     5
      #   /  \
      #   3   6
      # /  \   \
      # 2  4    7
      # /
      # 1
  for value in list_new_values:
    x = Node(value)
    balanced_tree.insert(balanced_tree.root, x)
  balanced_tree.inorder_traversal(balanced_tree.root)
  print balanced_tree.is_balanced(balanced_tree.root)

  list_path = balanced_tree.root_to_leaf_path([], balanced_tree.root, [])
  print "list path: ", list_path




