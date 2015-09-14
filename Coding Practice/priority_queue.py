__author__ = 'pratik'
def heapsort(list_val):
list_vals = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
h = []
for value in list_vals:
  heappush(h, value)
return [heappop(h) for i in range(len(h))]