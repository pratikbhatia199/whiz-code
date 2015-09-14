__author__ = 'pratik'
from copy import copy
set_values = [1, 2, 3]

def subsets_of_set(set_values, current_index, list_permutations):
  print "subsets of set"
  if current_index >= len(set_values):
    return list_permutations
  len_list_value = len(list_permutations)
  list_index = 0
  while list_index < len_list_value:
    temp_list = copy(list_permutations[list_index])
    temp_list.append(set_values[current_index])
    print "temp list: ", temp_list
    print "list permutations: ", list_permutations
    list_permutations.append(temp_list)
    list_index += 1
  current_index += 1
  return subsets_of_set(set_values, current_index, list_permutations)



if __name__ == '__main__':
  print "main name"
  print "set values: ", set_values[1]
  return_value = subsets_of_set(set_values, 0, list_permutations=[[]])
  print "return value: ", return_value