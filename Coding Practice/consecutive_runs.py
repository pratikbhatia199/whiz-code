__author__ = 'pratik'
def consecutive_runs(array_numbers):
  if len(array_numbers) < 3:
    return None

  answer = []
  current = array_numbers[0] - array_numbers[1]
  for i in range(1, len(array_numbers)-1):
    prev = current
    current = array_numbers[i] - array_numbers[i+1]
    if prev == 1:
      if current == 1:
        answer.append(i-1)
    if prev == -1:
      if current == -1:
        answer.append(i-1)
  print "answer: ", answer
  return answer

if __name__ == '__main__':
  print "inside main"
  consecutive_runs([1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7])