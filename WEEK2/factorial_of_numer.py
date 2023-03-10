# def factorial_number(n):
#    if n == 0:
#       return 1
#    else:
#       return n * factorial_number(n-1)
   
# print(factorial_number(5))


def factorial_number(n):
   if n == 0:
      return 1
   else:
      fact= 1
      while (n > 1):
         fact *= n
         n-= 1
      return fact

print(factorial_number(4))

def factorial_fraction(x):
   e=1
   while x > 0:
      e += (1/factorial_number(x))
      x-=1
   return e

print(factorial_fraction(5))

import math
#(2) fractional factorial
def factorial_e(n, x):
   e = 1
   while (n > 0):
      e += ((x**(n))/factorial_number(n))
      n -= 1
      exp_ans= (e)**(1/x)
   return exp_ans

print(factorial_e(5, 2))

