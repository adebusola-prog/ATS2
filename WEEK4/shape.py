class Rectangle:
    
   def __init__(self, no_of_sides, length, breadth):
      self.no_of_sides=no_of_sides
      self.length=length
      self.breadth=breadth

   def area(self):
      return self.length * self.breadth

   def perimeter(self):
      return 2*(self.length + self.breadth) 
   

class Square:

   def __init__(self, no_of_sides, length):
      self.no_of_sides=no_of_sides
      self.length=length

   def area(self):
      return self.length **2

   def perimeter(self):
      return 4*self.length

rectangle=Rectangle(4, 3, 2) 
print(f"{rectangle.area()}m2")
print(f"{rectangle.perimeter()}m")

square=Square(4, 5)
print(f"{square.area()}m2")
print(f"{square.perimeter()}m")