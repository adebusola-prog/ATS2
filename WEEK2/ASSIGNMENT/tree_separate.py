def create_star(n):
   for i in range(1, n+1):
      print(i * "* ")

# create_star(10)

def create_star_reverse(n):
   x=10
   while (x < n and x != 0):
      print(x * "* ")
      x -= 1 

# create_star_reverse(11)

def reverse_star(n):
   x=1
   z=9
   while (x < n and x != 0):
      y= x * "  " + z * (" *")
      x += 1
      z -=1
      print(y)

# reverse_star(10)

def star_reverse(n):
   x= 9
   y =1
   while (y < n and y !=0):
      z = x * ("  ") + y * (" *")
      x -= 1
      y += 1
      print(z)

# star_reverse(10)