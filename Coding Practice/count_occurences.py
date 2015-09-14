__author__ = 'pratik'

sorted_array = [0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
def count_occurences(sorted_array, key, low, high):
  mid = (low + high)/2
  if sorted_array[mid] < sorted_array[key]:
    print key, "less than"
    return count_occurences(sorted_array, key, mid+1, high)
  if sorted_array[mid] > sorted_array[key]:
    print key, "greater than"
    return count_occurences(sorted_array, key, low, mid-1)
  if sorted_array[mid] == key:
    print key, "found"
    low_val = find_lower_bound(sorted_array, low, high, key)
    high_val = find_upper_bound(sorted_array, low, high, key)
    return low_val, high_val


def find_lower_bound(sorted_array, key, low, high):
  print "find lower bound"
  mid = (high + low)/2
  if mid == 0:
    return 0
  if sorted_array[mid] == key:
    print "found something"
    if sorted_array[mid-1] < sorted_array[mid]:
      return mid
    else:
      return find_lower_bound(sorted_array, key, low, mid-1)



def find_upper_bound(sorted_array, key, low, high):
  print "find upper bound"
  mid = (high + low)/2
  if mid == len(sorted_array) -1:
    return mid
  if sorted_array[mid] == key:
    print "found nothing"
    if sorted_array[mid-1] > sorted_array[mid]:
      return mid
    else:
      return find_upper_bound(sorted_array, key, mid+1, high)


if __name__ == '__main__':
  sorted_array = [0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
  values = count_occurences(sorted_array, 1, 0, len(sorted_array)-1)
  print "values: ", values


