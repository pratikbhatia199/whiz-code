__author__ = 'pratik'
flag_array = [-1,0,1,-1,1,0]

def sort_flag(flag_array):
  print "sorting flag array: ", flag_array
  i = 0
  low = 0
  high = len(flag_array)
  mid = (low + high)/2
  while(i < len(flag_array)):
    print "value", flag_array[i]
    i += 1
    if flag_array[i] == 0:
      print "zero found"
      i = i+1

if __name__ == '__main__':
  print "Name is main"
  sort_flag(flag_array)