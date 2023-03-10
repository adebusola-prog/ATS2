number_1= int(input("enter the first number :"))
number_2= int(input("enter the second number :"))
number_3= int(input("enter the third number :"))

def quadratic_equation(a, b, c):
   factors= []
   middle_term=[]
   product_a_c= a * c
   for factor in range(-abs(product_a_c), abs(product_a_c) + 1):
      if factor != 0 and product_a_c % factor == 0:
         factors.append(factor)
   for factor in factors:
      for i in range(len(factors)):
         if factor + factors[i] == b and factor * factors[i] == product_a_c:
            middle_term.append(factor)
   print(middle_term)
   
   if a > 1 or a < 0:
      print(f"{-(middle_term[0])/a} and {-(middle_term[1])/a}")

   elif a ==1:
      print(f"{-(middle_term[0])} and {-(middle_term[1])}")

   else:
      print("cannot be solved by factorization")  

quadratic_equation(number_1, number_2, number_3)