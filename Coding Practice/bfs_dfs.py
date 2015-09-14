__author__ = 'pratik'
from collections import deque
dict_graph = {
  'v': ['r'],
  'r': ['v', 's'],
  'w': ['s', 't', 'x'],
  't': ['w', 'x', 'u'],
  'u': ['t', 'x', 'y'],
  's': ['r', 'w'],
  'x': ['w', 't', 'u', 'y'],
  'y': ['x', 'u']
}

set_visited = set()
queue = deque()
def bfs(queue):
  if len(queue) > 0:
    node = queue.popleft()
    if node not in set_visited:
      print "Node: ", node
      for adj_node in dict_graph[node]:
        if node not in set_visited:
          queue.append(adj_node)
      set_visited.add(node)
    bfs(queue)


stack = []

dict_dfs_graph = {
  'u': ['x', 'v'],
  'v': ['y'],
  'x': ['v'],
  'y': ['x'],
  'w': ['y', 'z'],
  'z': ['z']
}
set_visited_dfs = set()
set_visiting_dfs = set()

def dfs(node):
  if node not in set_visited_dfs and node not in set_visiting_dfs:
    set_visiting_dfs.add(node)
    for adj_node in dict_dfs_graph[node]:
      dfs(adj_node)
    print "Depth First Search: ", node








if __name__ == '__main__':
  queue.append('s')
  bfs(queue)
  dfs('u')
  for node in dict_dfs_graph:
    if node not in set_visited_dfs:
      dfs(node)










