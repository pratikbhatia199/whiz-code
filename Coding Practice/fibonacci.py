__author__ = 'pratik'
dict_fibo = {}
dict_fibo[0] = 1
dict_fibo[1] = 1
def fibonacci(number, list_integers):
  print "fibonacci", number


  if number in dict_fibo:
    return dict_fibo[number]
  dict_fibo[number] = (
                        fibonacci(number-1, list_integers) +
                        fibonacci(number-2, list_integers)
  )
  return dict_fibo[number]

if __name__ == '__main__':
  value = fibonacci(4, [] )
  print value