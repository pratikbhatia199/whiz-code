__author__ = 'pratik'
A = [1, 3, 5, 7, 0, 0, 0, 0]
B = [2, 4, 6, 8]

b_index = len(B) - 1
a_index = len(A) - 1
a_end = 3
while b_index >= 0:
  if A[a_end] > B[b_index]:
    A[a_index] = A[a_end]
    a_index -= 1
    a_end -= 1
  else:
    A[a_index] = B[b_index]
    a_index -= 1
    b_index -= 1

print "a", A


