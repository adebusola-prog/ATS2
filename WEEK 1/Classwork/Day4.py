# model a classroom with these three data structures: Tuple, list, dictionary

# fname, lastname, height, weight, birth year, gender

import datetime

today = datetime.date.today()

year = int(today.strftime("%Y"))


classroom_list=[
   ["Adebusola", "Adeyeye", 4.5, 45, 1997, "female"],
   ["Daniel", "Victor", 6.0, 70, 1998, "male"],
   ["Taofeeq", "Olaitan", 6.5, 80, 1996, "male"],
   ["Yetunde", "Adeoti", 5.5, 50, 1999, "female"],
   ["Adeola", "Ahmed", 4.0, 65, 1994, "male"]
]

# List of ages
Adebusola_age=year-classroom_list[0][4]
print(Adebusola_age)
Daniel_age=year-classroom_list[1][4]
print(Daniel_age)
taofeeq_age=year-classroom_list[2][4]
print(taofeeq_age)
Yetunde_age=year-classroom_list[3][4]
print(Yetunde_age)
Adeola_age=year-classroom_list[4][4]
print(Adeola_age)

# list of bmis
adebusola_bmi=classroom_list[0][3] /classroom_list[0][2]**2
print(round(adebusola_bmi))
Daniel_age=classroom_list[1][3] /classroom_list[1][2]**2
print(round(Daniel_age))
taofeeq_bmi=classroom_list[2][3]/classroom_list[2][2]**2
print(round(taofeeq_bmi))
yetunde_bmi=classroom_list[3][3]/classroom_list[3][2]**2
print(round(yetunde_bmi))
adebusola_bmi=classroom_list[4][3]/classroom_list[4][2]**2
print(round(adebusola_bmi))



classroom_tuple=(
   ("Adebusola", "Adeyeye", 4.5, 45, 1997, "female"),
   ("Daniel", "Victor", 6.0, 70, 1998, "male"),
   ("Taofeeq", "Olaitan", 6.5, 80, 1996, "male"),
   ("Yetunde", "Adeoti", 5.5, 50, 1999, "female"),
   ("Adeola", "Ahmed", 4.0, 65, 1994, "male")
)
# tuple_ages
Adebusola_age=year-classroom_tuple[0][4]
print(Adebusola_age)
Daniel_age=year-classroom_tuple[1][4]
print(Daniel_age)
taofeeq_age=year-classroom_tuple[2][4]
print(taofeeq_age)
Yetunde_age=year-classroom_tuple[3][4]
print(Yetunde_age)
Adeola_age=year-classroom_tuple[4][4]
print(Adeola_age)

# tuple_bmi
adebusola_bmi=classroom_tuple[0][3] /classroom_tuple[0][2]**2
print(round(adebusola_bmi))
Daniel_age=classroom_tuple[1][3] /classroom_tuple[1][2]**2
print(round(Daniel_age))
taofeeq_bmi=classroom_tuple[2][3]/classroom_tuple[2][2]**2
print(round(taofeeq_bmi))
yetunde_bmi=classroom_tuple[3][3]/classroom_tuple[3][2]**2
print(round(yetunde_bmi))
adebusola_bmi=classroom_tuple[4][3]/classroom_tuple[4][2]**2
print(round(adebusola_bmi))




classroom_dict={
   "std1":{"f_name": "Adebusola", "last_name": "Adeyeye", "height": 4.5, "weight": 45, "birth_year":1997, "gender": "female"},
   "std2":{"f_name": "Daniel", "last_name": "Victor", "height": 6.0, "weight": 70, "birth_year":1998, "gender": "male"},
   "std3":{"f_name": "Taofeeq", "last_name": "Olaitan", "height": 6.5, "weight": 80, "birth_year":1996, "gender": "male"},
   "std4":{"f_name": "Yetunde", "last_name": "Adeoti", "height": 5.5, "weight": 50, "birth_year":1999, "gender": "female"},
   "std5":{"f_name": "Adeola", "last_name": "Ahmed", "height": 4.0, "weight":65, "birth_year":1994, "gender": "male"},
}
# Dictionary
list_ages= []
std1_age= year - classroom_dict["std1"]["birth_year"]
std2_age= year - classroom_dict["std2"]["birth_year"]
std3_age= year - classroom_dict["std3"]["birth_year"]
std4_age= year - classroom_dict["std4"]["birth_year"]
std5_age= year - classroom_dict["std5"]["birth_year"]
list_ages.append(std1_age)
list_ages.append(std2_age)
list_ages.append(std3_age)
list_ages.append(std4_age)
list_ages.append(std5_age)

print(list_ages)

# BMI
list_bmis=[]
std1_bmi= round(classroom_dict["std1"]["weight"]/classroom_dict["std1"]["height"] ** 2)
std2_bmi= round(classroom_dict["std2"]["weight"]/classroom_dict["std2"]["height"] ** 2)
std3_bmi= round(classroom_dict["std3"]["weight"]/classroom_dict["std3"]["height"] ** 2)
std4_bmi= round(classroom_dict["std4"]["weight"]/classroom_dict["std4"]["height"] ** 2)
std5_bmi= round(classroom_dict["std5"]["weight"]/classroom_dict["std5"]["height"] ** 2)

list_bmis.append(std1_bmi)
list_bmis.append(std2_bmi)
list_bmis.append(std3_bmi)
list_bmis.append(std4_bmi)
list_bmis.append(std5_bmi)

print(list_bmis)



