# lat1, long1  = 57.792017, 12.054745
# lat2, long2  = -14.896547, -3.132567
 
# x=['North', 'S'][lat1 < 0]
# print(x[3])
# print(['N', 'S'][lat2 < 0])
 
# print(['E', 'W'][long1 < 0])
# print(['E', 'W'][long2 < 0])


# import string
# letters = string.ascii_letters
# vowel_letters ="aeiou"
# consonant_letters="bcdfghjklmnpqrstvwxyz"

# word= input("enter a word").lower()
# x= [f"{word} is not a letter", f"{word[0]} starts with a vowel"] [word[0] in letters]

# word=float(input("enter a number"))
# print(word)



# A program that takes a word and prints if it starts with a vowel or a consonant

# A program that takes 5 letter word and prints each letter and say if it
#  is a vowel or a consonant(Do not use loop, you can try to avoid if and else)






# x= "aba, bbsbsb"
# print(x.split("ba"))





# colors=["yellow", "red", "green", "blue", "violet"]
# colors.sort(key=len)

# print(colors)














# n= 173442.12356
# print(f"the value n is {n:.2f} ")
# print(f"the value of n is {n:,.2f}")

# m = 0.9
# print(f"The pecentage of m is {m:.4%} ")

# def multiply(x, y):
#    '''Returns the product of x and y'''
#    product= x * y
#    return product
    
# print(multiply(5,6))
# (help(multiply))

# num=float(input("enter a positive number"))
# while num <=0:
#    print("This is a negative number")

#    num=float(input("enter a positive number"))

# grade = 70
# if grade >= 70:
#    print("You passed the class!")
# if grade < 70:
#    print("You did not pass the class :(")
# print("Thank you for attending.")


# for n in range(3):
#    password= input("enter your password")
#    if password == "I<3beiber":
#       break
#    print("password is incorrect")

# else:
#    print("You are a fraud")

# number= int(input("enter a number"))
# print(type(number))
# print(int("-4k"))

# def divide_(num1, num2):
#    try:
#       x=num1 / num2
#       return x
#    except TypeError:
#       print("both num1 and num2 must be an integer")
#    except ZeroDivisionError:
#       print("num 2 should be a number and not zero")

# print(divide_(3, 4))


# import random
# def toss_coin():
#    if random.randint(0, 1) == 0:
#       return "heads"
#    else:
#       return "tail"

# print(toss_coin())


# heads_tally=0
# tails_tally= 0
# for trial in (0, 10_000):
#    if toss_coin() == "heads":
#       heads_tally += 1
#    else:
#       tails_tally += 1

# print(heads_tally)
# print(tails_tally)
# ratio=heads_tally/tails_tally
# print(ratio)

# print(tuple("python"))



# universities = [
# ['California Institute of Technology', 2175, 37704],
# ['Harvard', 19627, 39849],
# ['Massachusetts Institute of Technology', 10566, 40732],
# ['Princeton', 7802, 37000],
# ['Rice', 5879, 35551],
# ['Stanford', 19535, 40569],
# ['Yale', 11701, 40500]
# ]


# def university_detail(n):
#    return n

# print(university_detail(universities[1][2]))
# print(university_detail(universities[4]))

# import random
# noun=["ade", "ola", "ope", "tayo", "ola"]
# adv= ["silently", "gently", "sparingly", "redily"]
# for i in range(3):
#    x=random.choice(noun)
#    for j in range(3):
#       y=random.choice(adv)

#    print(x, y)


# x= 1==11
# print(x)


# print("x")

# def invest(amount, rate, years):
#     """Display year on year growth of an initial investment"""
#    for year in range(1, years + 1):
#       amount = amount * (1 + rate)
#       print(f"year {year}: ${amount:,.2f}")


# amount = float(input("Enter a principal amount: "))
# rate = float(input("Enter an anual rate of return: "))
# years = int(input("Enter a number of years: "))

# invest(amount, rate, years)

# import random
# def roll_dice():
#     die1= random.randrange(1, 7)
#     die2= random.randrange(1, 7)

#     return (die1, die2)


# def display_dice(dice):
#     die1, die2 = dice
#     print(f"Played roll dice {die1} + {die2} = {sum(dice)}")


# die_values= roll_dice()
# display_dice(die_values)

# print(die_values)
# sum_of_dice = sum(die_values)
# print(sum_of_dice)import requests

#the required first parameter of the 'get' method is the 'url':

# import requests
# x = requests.get('https://w3schools.com/python/demopage.htm')

# #print the response text (the content of the requested file):
# print(x.text)

# converting binary to decimal



def factorial_number(n):
   if n== 0 or n == 1:
      return 1
   else:
      return n * factorial_number(n-1)

# print(factorial_number(5))

def fac(n):
   if n==0 or n == 1:
      return 1
   elif n < 0:
      print("you cant have a negative factorial")
   else:
      fact = 1
      while (n > 1):
        
         fact *= n
         n -= 1
      return fact

# print(fac(5))





def factorial_e(n, x):
   e = 1
   while (n > 0):
      e += ((x**(n))/factorial_number(n))
      n -= 1
   return e

# print(factorial_e(10, 2))


def get_factorial(n):
   if n == 0:
      return 1
   elif n < 0:
      return("no negative factorial")
   else:
      fact= 1
      for i in range(1, n +1):
         fact *= i
      return fact

print(get_factorial(6))

























