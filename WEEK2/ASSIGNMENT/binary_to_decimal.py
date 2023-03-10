binary_to_decimal=[]
binary_used=[]

def binary_decimal(binary_input):
   for i in binary_list:
      y=int(i)
      binary_used.append(y)
   print(binary_used)
   binary_index= len(binary_list) -1
   for i in binary_used:
      x= i * 2**(binary_index)
      binary_index -= 1
      binary_to_decimal.append(x)
   print(sum(binary_to_decimal))

binary_input= int(input("enter the binary to be converted: "))
binary_list=list(str(binary_input))

binary_decimal(binary_input)



# converting decimal to binary
def binary_to_decimal(binary):
   i=  0
   decimal = 0
   while(binary != 0):
      remainder = binary % 10
      decimal = decimal + remainder * pow(2, i)
      
      binary = binary//10
      i +=1
   print(decimal)


binary_to_decimal(101)





























