__author__ = 'pratik'
number_of_steps = 0
dict_steps = {}
def number_of_steps(steps, dict_steps):
  print "this gives number of steps"
  if steps < 0:
    return 0

  if steps in dict_steps:
    return dict_steps[steps]

  dict_steps[steps] = number_of_steps(steps-1, dict_steps) \
                      + number_of_steps(steps-2, dict_steps)\
                      + number_of_steps(steps-3, dict_steps)
  return dict_steps[steps]

if __name__ == '__main__':
  steps = 5
  dict_steps[0] = 0
  dict_steps[1] = 1
  dict_steps[2] = 2
  dict_steps[3] = 3
  steps = number_of_steps(steps, dict_steps)
  print "steps: ", steps