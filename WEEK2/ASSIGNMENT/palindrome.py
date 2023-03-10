num = int(input("enter a number : "))
number_cal= num
reverse = 0

while number_cal != 0:
   reverse= (reverse * 10) + (number_cal % 10)
   number_cal = number_cal // 10

if num == reverse:
   print("number is a palindrome")

else:
   print("number is not a palindrome")




