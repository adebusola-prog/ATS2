x= [1,2,3,4,5,6,7,8,9]
y=[0]
x.extend(y)
x.join(y)
print(x)
for i in range(len(x)):
   print(x[i] *2)


for x in range(0, 9, 2):
   print(x)

even=[]
odd=[]
def even_odd(n):
   for i in n:
      if i % 2 == 0:
         print(f"{i} is even")
         even.append(i)
         
      else:
         print(f"{i} is odd")
   print(len(even))
   print(len(odd))

# even_odd([1, 2, 10, 5, 7, 8, 4, 15, 20])
import random
print(random.randrange(0, 12, 2))


# Given a List of subject, objects and verbs, generate a sentence in which 
# at least one word from each item is included in the generated sentence