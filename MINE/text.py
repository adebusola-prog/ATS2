# import csv
# def read_csv(file_name):
#    with open(file_name, "r") as x:
#       read = csv.DictReader(x)
#       return list(read)



# alphabets_lower= "abcdefghijklmnopqrstuvwxyz"
# alphabets_upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numbers= ["0","1","2","3","4","5","6","7","8","9"]

# letter_list1= (list(alphabets_lower))
# letter_list2= (list(alphabets_upper))


# # x=int(input("enter your padding number"))
# def en_crypt(n:str, x):

#    v=[]
#    for i in n:
#       if i in (" "):
#          v.append(i)
#       if i in letter_list1:
#          letter_position=letter_list1.index(i)
#          encryption1= (letter_position - x) % 26
#          aswer=letter_list1[encryption1].swapcase()
#          v.append(aswer)
   

#       if i in letter_list2:
#          letter_position2=letter_list2.index(i)
#          encryption2= (letter_position2 - x) % 26
#          aswer2=letter_list2[encryption2].swapcase()
#          v.append(aswer2)
  

#       if i in numbers:
#          number_position=numbers.index(i)
#          encryption3= (number_position -x) % 10
#          answer3= numbers[encryption3] 
#          v.append(answer3)
#          global encrypted_result
#    encrypted_result=''.join(v)
   
#    return(encrypted_result)

# # en_crypt("I am a Good b58y to The main", 55)


# def decrypt(n, x):
   
#    v=[]
#    for i in n:
#       if i in (" "):
#          v.append(i)
#       if i in letter_list1:
#          letter_position=letter_list1.index(i)
#          encryption1= (letter_position + x) % 26
#          aswer=letter_list1[encryption1].swapcase()
#          v.append(aswer)

#       if i in letter_list2:
#          letter_position2=letter_list2.index(i)
#          encryption2= (letter_position2 + x) % 26
#          aswer2=letter_list2[encryption2].swapcase()
#          v.append(aswer2)

#       if i in numbers:
#          number_position=numbers.index(i)
#          encryption3= (number_position + x) % 10
#          answer3= numbers[encryption3]
#          v.append(answer3)

#    return(''.join(v))
   
#    # en_crypt(n, x)

# decrypt(encrypted_result, 55)


# class Customer:
   
#    def __init__(self, database):
#       self.database=database
   

#    def __repr__(self):
#       return str(self.database)

#    def sign_in(self):
#       username=input("enter your username")
#       password= input("enter your password")
#       for info in self.database:
#          if info['username'] == username and info['password'] == password:
#             print(info['username'])
#             # print(decrypt(type(info['password'], 58)))
#             x=(decrypt(info['password'], 58))
#             print(type(x))
#             # write_log_csv(username, f"{username} signed in" )
#             print("you are welcome", username)
#             return

#       else:
#          print("Username does not match password")
#          print("try again")


# customer=Customer(read_csv('app.csv'))
# # print(customer)
# print(customer.sign_in())

import random_multiplication

value= random_multiplication.multiply_number(13, 56)

