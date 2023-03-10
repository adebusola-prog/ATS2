
alphabets_lower= "abcdefghijklmnopqrstuvwxyz"
alphabets_upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers= ["0","1","2","3","4","5","6","7","8","9"]

letter_list1= (list(alphabets_lower))
letter_list2= (list(alphabets_upper))


# x=int(input("enter your padding number"))
def en_crypt(n:str, x):

   v=[]
   for i in n:
      if i in (" "):
         v.append(i)
      if i in letter_list1:
         letter_position=letter_list1.index(i)
         encryption1= (letter_position - x) % 26
         aswer=letter_list1[encryption1].swapcase()
         v.append(aswer)
   

      if i in letter_list2:
         letter_position2=letter_list2.index(i)
         encryption2= (letter_position2 - x) % 26
         aswer2=letter_list2[encryption2].swapcase()
         v.append(aswer2)
  

      if i in numbers:
         number_position=numbers.index(i)
         encryption3= (number_position -x) % 10
         answer3= numbers[encryption3] 
         v.append(answer3)
         global encrypted_result
   encrypted_result=''.join(v)
   
   return(encrypted_result)

print(en_crypt("Admin", 55))


def decrypt(n, x):
   
   v=[]
   for i in n:
      if i in (" "):
         v.append(i)
      if i in letter_list1:
         letter_position=letter_list1.index(i)
         encryption1= (letter_position + x) % 26
         aswer=letter_list1[encryption1].swapcase()
         v.append(aswer)

      if i in letter_list2:
         letter_position2=letter_list2.index(i)
         encryption2= (letter_position2 + x) % 26
         aswer2=letter_list2[encryption2].swapcase()
         v.append(aswer2)

      if i in numbers:
         number_position=numbers.index(i)
         encryption3= (number_position + x) % 10
         answer3= numbers[encryption3]
         v.append(answer3)

   print(''.join(v))
   
   # en_crypt(n, x)

decrypt(encrypted_result, 55)
 