import random
def multiply_number(n, k):
   first_digit= random.randint(1, n)
   second_digit= random.randint(1, k)
   print(f"{first_digit} * {second_digit}")
   computer_answer= first_digit * second_digit

   while True:
      user_answer= int(input("enter your answer"))
      if user_answer == computer_answer:
         print("Very Good")
         multiply_number(n, k)
      else:
         print("No, please try again")

      
# multiply_number(10, 10)





# people =[{"f_name":"Faith", "l_name":"Adeosun", "day_month": "1st of January", "attendance": 30, "height": 126, "weight": 60, "age": 25},
#          {"f_name":"Toluwanimi", "l_name":"Ogunbiyi", "day_month": "2nd of May", "attendance": 30, "height":126 , "weight": 50, "age": 25},
#          {"f_name":"Lukman", "l_name":"Abisoye", "day_month": "3rd of October", "attendance": 30, "height": 118, "weight": 60, "age": 24},
#          {"f_name":"Ahmad", "l_name":"Sarafudeen", "day_month": "4th of July", "attendance": 30, "height": 129, "weight": 80, "age": 24},
#          {"f_name":"Abdullaih", "l_name":"Salam", "day_month": "5th of June", "attendance": 30, "height": 110, "weight": 70, "age": 25},
#          {"f_name":"Basheer", "l_name":"Balogun", "day_month": "6th of November", "attendance": 30, "height": 131, "weight": 70, "age": 26},
#          {"f_name":"Adebusola", "l_name":"Adeyeye", "day_month": "7th of August", "attendance": 30, "height": 122, "weight": 60, "age": 27},
#          {"f_name":"Awwal", "l_name":"Adeleke", "day_month": "8th of December", "attendance": 30, "height": 146,  "weight": 80, "age": 26},
#          {"f_name":"Tajudeen", "l_name":"Abdullai", "day_month": "9th of September", "attendance": 30, "height": 137, "weight": 60, "age": 25},
#          {"f_name":"Abraham", "l_name":"Adekunle", "day_month": "15th of May", "attendance": 30, "height": 138, "weight": 70, "age": 26},
#          {"f_name":"Yusuf", "l_name":"Oyedele", "day_month": "13th of March", "attendance": 30, "height": 140, "weight": 60, "age": 27}]

# # for i in people:
# #    print(i)

# for j in range(len(people)):
#    # print(people[j])
#    for k in range(len(people)):
#       if people[j]['height'] != people[k]['height']:
#          print(people[j])


























