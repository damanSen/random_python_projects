print('Program  to deal with different types of errors')

import time
try:
  numerator = int(input('Enter a number to divide:  '))
  denominator = int(input('Enter a number to divide by:  '))
  answer = numerator/denominator
  time.sleep(1)
  print(answer)
except ZeroDivisionError:
  time.sleep(1)
  print('Cannot be divide by zero')
except ValueError:
  time.sleep(1)
  print('Enter only numbers please')
except Exception:
  time.sleep(1)
  print('Something went wrong')
