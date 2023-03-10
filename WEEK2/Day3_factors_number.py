# a function that takes a number and prints factors of all numbers betwee 1 and the number
# import math
def factors_number(n):
   for i in range(1, n+1):
      factors=[]
      for j in range(1, (i//2) + 1):
         if i % j == 0:
            factors.append(j)
      factors.append(i)       
      print(f"factors of {i} is {factors}")
    
factors_number(100)


def factor_number(n):
   
   start= 0
   while start < n + 1:
      start2= 1
      factors=[]
      while start2 < (start +1):
         if start % start2 == 0:
            factors.append(start2)
         start2 += 1
      start +=1
      print(factors)

# factor_number(10)



def factors_number(n):
   i=1
   while i < ((n//2) + 1):
      j= 1
      factors= []
      while j < ((i//2) + 1):
         if j % i == 0:
            factors.append(j)
         j += 1
      i += 1
      print(factors)

factor_number(100)





































