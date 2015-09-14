__author__ = 'pratik'

def binary_search(list_values, key, low, high):
  if low > high:
    return None
  mid = (low + high)/2
  print "mid", list_values[mid]
  if list_values[mid] == key:
    return mid

  if list_values[mid] > key:
    return binary_search(list_values, key, low, mid-1)

  if list_values[mid] < key:
    return binary_search(list_values, key, mid+1, high)



x = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

index = binary_search(x, 2, 0, len(x) - 1)
print "index: ", index