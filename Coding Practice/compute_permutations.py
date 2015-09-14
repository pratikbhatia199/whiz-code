# __author__ = 'pratik'
# from copy import copy
# list_numbers = [1, 2, 3]
# def compute_permutations(list_permutations, current_index):
#   print "computing permutations", list_permutations, current_index
#   if current_index == len(list_numbers):
#     return list_permutations
#
#   current_char = list_numbers[current_index]
#   len_list_permutations = len(list_permutations)
#   print "len_list_permutations: ", len_list_permutations
#   for i in range(0, len_list_permutations):
#     len_list_value = len(list_permutations[i])
#     print "len_list_value: ", len_list_value
#     for current_index in range(0, len_list_value):
#       print "len list value: ", len_list_value
#       print "current_index: ", current_index
#
#       list_value = copy(list_permutations[i])
#       print "list_value: ", list_value
#       list_value.insert(current_index, current_char)
#       list_permutations.append(list_value)
#       print "list_permutations: ", list_permutations
#     print "current char: ", current_char
#     list_permutations[i].append(current_char)
#     print "after appending: ", list_permutations
#   return compute_permutations(list_permutations, current_index + 1)
#
# if __name__ == '__main__':
#   values = compute_permutations([[1]], 1)
#   print values
