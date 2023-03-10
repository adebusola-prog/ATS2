def person_name(name):
   print(f"Welcome, {name}")

# person_name("Adebusola")


def arithmetic(x:int, y:int):
   print(x * y)
   print(x - y)
   print(x/y)
   print(x + y)
   print(x ** y)

# num1= int(input("enter first number"))
# num2= int(input("enter second number"))
# arithmetic(num1, num2)


def factor_number(a, b):
   if a % b == 0:
      print(f"{b} is a factor of {a}")
   else:
      print(f"{b} is not factor of {a}")

# factor_number(34, 4)

pie= 3.142
def circle_calc(radius):
   print(2 * pie* radius)
   print(pie*(radius**2))
   print(radius *2)

# circle_calc(7)



def credentials(user_name1, pass_word1, user_name2, pass_word2):
   if user_name1== user_name2 and pass_word1==pass_word2:
      print("You are logged in")
   else:
      print("wrong credentials")

# username= input("enter your username").lower()
# password=input("enter your password")
# username2=input("enter your user name again").lower()
# password2=input("enter your password again")

# credentials(username, password, username2, password2)
import datetime

today = datetime.date.today()

year = int(today.strftime("%Y"))

class_profile= {
   "Adebusola":{"first_name": "Adebusola", "last_name": "Adeyeye", "birth":{"month":"Feburary", "day":5}, "attendance":90, "height": 1.5, "weight":45, "age":26},
   "Afolabi":{"first_name": "Afolabi", "last_name": "Oredipe", "birth":{"month":"Feburary", "day":23}, "attendance":5, "height": 1.6, "weight":50, "age":26},
   "Feranmi":{"first_name": "Feranmi", "last_name": "Adeyemi", "birth":{"month":"January", "day":4}, "attendance":9, "height": 1.55, "weight":66, "age":27},
   "Daniel":{"first_name": "Daniel", "last_name": "Olayinka", "birth":{"month":"May", "day":23}, "attendance":10, "height": 1.3, "weight":78, "age":26},
   "Yetunde":{"first_name": "Yetunde", "last_name": "Opeoluwa", "birth":{"month":"October", "day":12}, "attendance":11, "height": 1.2, "weight":90, "age":24},
   "Taofeeq":{"first_name": "Taofeeq", "last_name": "Adigun", "birth":{"month":"September", "day":3}, "attendance":12, "height": 1.1, "weight":67, "age":22},
   "Abdulgafar":{"first_name": "Abdulgafar", "last_name": "Ahmed", "birth":{"month":"October", "day":9},"attendance":14, "height": 1.3, "weight":89, "age":20},
}

def attendance_increment(data):
   class_profile[data]["attendance"] += 1
   print(class_profile)

# attendance_increment("Adebusola")

def name_update(initial_first_name, new_first_name, new_last_name):
   class_profile[initial_first_name]["first_name"]= new_first_name
   class_profile[initial_first_name]["last_name"] = new_last_name
   # class_profile[new_first_name] = class_profile.pop(initial_first_name)
   print(class_profile)

# name_update('Adebusola', "Ope", "Pelu")

def name_title(class_profile):
   for i in class_profile:
      x = class_profile[i]["first_name"] + " " + class_profile[i]["last_name"] 
      print(x.title())
      return class_profile

# print(name_title(class_profile))

def new_profile(data):
   class_profile[data] = {"first_name": "Yomi", "last_name":"Temitope", "birth":{"month":"May", "day":23}, "attendance":10, "height": "1.3", "weight": 78, "age":26}
   return class_profile

print(new_profile("Oke"))

def number_std(class_profile):
   return len(class_profile)

# print(number_std(class_profile))

def remove_profile(data):
   class_profile.pop(data)
   return class_profile

# print(remove_profile("Adebusola"))

def birth_month(data):
   return class_profile[data]["birth"]["month"]
   
# print(birth_month("Yetunde"))

def profile_initials(class_profile):
   for i in class_profile:
      print(class_profile[i]["first_name"][0] + "." + class_profile[i]["last_name"][0])

# profile_initials(class_profile)


def bmi_profile(class_profile):
   for i in class_profile:
      bmi= class_profile[i]["weight"] / (class_profile[i]["height"] ** 2)
      print(bmi)
   

# bmi_profile(class_profile)


min_age_list=[]
def min_age(class_profile):
   for i in class_profile:
      age= class_profile[i]["age"]
      min_age_list.append(age)
   print(min(min_age_list))

# min_age(class_profile)


max_age_list=[]
def max_age(class_profile):
   for i in class_profile:
      age= class_profile[i]["age"]
      max_age_list.append(age)
   print(max(max_age_list))

# max_age(class_profile)


age_list=[]
def average_age(class_profile):
   for i in class_profile:
      age= class_profile[i]["age"]
      age_list.append(age)
   print(sum(age_list)/len(age_list))

# average_age(class_profile)


def birth_year(class_profile):
   for i in class_profile:
      birth_year= year- class_profile[i]["age"]
      print(birth_year)

# birth_year(class_profile)


# function that group profile by birth month
# import calendar
# for k in range(0, 13):
#   x_year=calendar.month_name[k]
#   print(x_year)

month_year= ["January", "Feburary", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"]
def group_by_month(class_profile):
   for y in month_year:
      for i in class_profile:
         if y in class_profile[i]["birth"]["month"]:
            print(f"{y}: {class_profile[i]}")

# group_by_month(class_profile)

# describe the class
"""The class consists of 7 students initially. A student was included to the profile which makes a total number of 8 students
the minimumage of the class is 20 and the maximum age is 27. The average age of the class is 24.4. A student was born in January.
More students are born in october and feburary"""

