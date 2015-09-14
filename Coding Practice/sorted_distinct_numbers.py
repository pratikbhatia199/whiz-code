__author__ = 'pratik'
list_magic = [-6, -5, -4, -3, -2, 5, 16, 17, 18, 19]

def find_magic_index(list_magic, low, high):
  if low > high:
    return -1
  mid = (low+high)/2
  print "magic index"
  if list_magic[mid] == mid:
    return mid
  if list_magic[mid] < mid:
    return find_magic_index(list_magic, mid+1, high)
  if list_magic[mid] > mid:
    return find_magic_index(list_magic, low, mid-1)

if __name__ == '__main__':
  index = find_magic_index(list_magic, 0, len(list_magic)-1)
  print 'magic index: ', index


