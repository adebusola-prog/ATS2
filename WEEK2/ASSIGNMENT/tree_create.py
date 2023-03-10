def create_star(rows):
   for i in range(1, rows+1):
      for j in range(0, i):
         print("* ", end="")
      for j in range(0, rows+1-i):
         print("  ", end="")
      for j in range(0, rows+1-i):
         print("* ", end="")
      for j in range(0, 2*i):
         print("  ", end="")
      for j in range(0, rows+1-i):
         print("* ", end="")
      for j in range(0, rows+1-i):
         print("  ", end="")
      for j in range(0, i):
         print("* ", end="")
      print()

create_star(10)