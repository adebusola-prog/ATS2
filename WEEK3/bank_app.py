import csv
import random
import pandas as pd
import csv
import datetime
import sys
today = datetime.datetime.today()

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

en_crypt("I am a Good b58y to The main", 55)


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

   return(''.join(v))
   
   # en_crypt(n, x)

decrypt(encrypted_result, 55)

def read_csv(file_name):
   with open(file_name, "r") as x:
      read = csv.DictReader(x)
      return list(read)


def write_adminlog_csv(admin, event):
   with open("admin_activity_logs.csv", "a", newline="\n") as x:
      header = ["Date_Time", "Admin", "Event"]
      write = csv.DictWriter(x, fieldnames=header)

      data = {
         "Date_Time": today,
         "Admin": admin,
         "Event": event,
      }

      if len(read_csv("admin_activity_logs.csv")) < 1:
         write.writeheader()
         write.writerow(data)
      else:
         write.writerow(data)


def write_stafflog_csv(staff, event):
   with open("staff_activity_logs.csv", "a", newline="\n") as x:
      header = ["Date_Time", "Staff", "Event"]
      write = csv.DictWriter(x, fieldnames=header)

      data = {
         "Date_Time": today,
         "Staff": staff,
         "Event": event,
      }

      if len(read_csv("staff_activity_logs.csv")) < 1:
         write.writeheader()
         write.writerow(data)
      else:
         write.writerow(data)


def read_csv(file_name):
   with open(file_name, "r") as x:
      read = csv.DictReader(x)
      return list(read)


def write_log_csv(customer, event):
   with open("customer_activity_logs.csv", "a", newline="\n") as x:
      header = ["Date_Time", "Customer", "Event"]
      write = csv.DictWriter(x, fieldnames=header)

      data = {
         "Date_Time": today,
         "Customer": customer,
         "Event": event,
      }

      if len(read_csv("customer_activity_logs.csv")) < 1:
         write.writeheader()
         write.writerow(data)
      else:
         write.writerow(data)
      

class Admin:

   @classmethod     
   def staff_db(cls, filename):
      with open(filename, "r") as x:
         read= csv.DictReader(x)
         return list(read)
   
   @classmethod  
   def admin_create_account(cls):
      with open("admin_db.csv", "a", newline="\n") as x:
         
         header =["firstname", "lastname", "username", "password"
         ]
         write=csv.DictWriter(x, fieldnames=header)

         f_name= input("enter your first_name")
         l_name=input("enter your last name")
         username=input("enter your username ")
         password=input("enter your password")
         
         data= {
               "firstname": f_name,
               "lastname": l_name,
               "username": username,
               "password": en_crypt(password, 58)
         }
         
         if len(cls.staff_db("admin_db.csv")) < 1:
            write.writeheader()
            write.writerow(data)
         else:
            write.writerow(data)

   def sign_in(self, username, password):
      admin_db=self.staff_db("admin_db.csv")
      self.username = username
      self.password = password
      for info in range(len(admin_db)):
         if admin_db[info]['username'] == self.username and decrypt(admin_db[info]['password'], 58) == self.password:
            write_log_csv(self.username, f"{self.username} signed in" )
            print("you are welcome", self.username)
            return

      else:
         print("Username does not match password")
         print("try again")
   
   @classmethod  
   def staff_create_account(cls):
      with open("staff_db.csv", "a", newline="\n") as x:
         
         header =["firstname", "lastname", "username", "password", "change_password", "status" 
         ]
         write=csv.DictWriter(x, fieldnames=header)

         f_name= input("enter your first_name ")
         l_name=input("enter your last name ")
         username=input("enter your username ")
         password=input("enter your password ")
         change_password=" "
         active="is_active"

         
         data= {
               "firstname": f_name,
               "lastname": l_name,
               "username": username,
               "password": password,
               "change_password": change_password,
               "status": active
         }
         
         if len(cls.staff_db("staff_db.csv")) < 1:
            write.writeheader()
            write.writerow(data)
         else:
            write.writerow(data)
         write_adminlog_csv("Admin", f"created staff, {username}'s account")

   def suspend_staff_account(self):
      username = input("enter the username to be suspended")
      self.username=username
      list_db=self.staff_db("staff_db.csv")
      for i in range(len(list_db)):
         if self.username == list_db[i]['username'] and list_db[i]['status'] == 'is_active':

            df = pd.read_csv('staff_db.csv')
            df.loc[list_db.index(list_db[i]), 'status'] = "not_active"
            df.to_csv('staff_db.csv', index=False) 
            print(f"{self.username} has been suspended")

         elif self.username == list_db[i]['username'] and list_db[i]['status'] == 'not_active':
            write_adminlog_csv("Admin", "suspended staff, {self.username}'s account")
            print("account was already suspended")


   def reactivate_staff_account(self):
      username = input("enter the username to be suspended")
      self.username=username
      list_db=self.staff_db("staff_db.csv")
      for i in range(len(list_db)):
         if self.username == list_db[i]['username'] and list_db[i]['status'] == 'not_active':

            df = pd.read_csv('staff_db.csv')
            df.loc[list_db.index(list_db[i]), 'status'] = "is_active"
            df.to_csv('staff_db.csv', index=False) 
            write_adminlog_csv("Admin", "reactivated staff, {self.username}'s account")

         elif self.username == list_db[i]['username'] and list_db[i]['status'] == 'is_active':
            
            print("account was activated before")

   def log_out(self):
      sys.exit()

class Customer:

   def __init__(self, database, username, password):
      self.database=database
      self.username = username 
      self.password = password

   def __repr__(self):
      return str(self.database)


   @classmethod     
   def customer_db(cls, filename):
      with open(filename, "r") as x:
         read= csv.DictReader(x)
         return list(read)


   def generate_digits(length):
      list_of_number = range(9)
      number = "308"
      for i in range(length):
         number += str(random.choice(list_of_number))
      return number 

   
   @classmethod  
   def customer_create_account(cls):
      with open("app.csv", "a", newline="\n") as x:
         
         header =["firstname", "lastname", "username", "phone_number", "account_number", "account_type", "account_balance", 
         "pin", "password"
         ]
         write=csv.DictWriter(x, fieldnames=header)

         f_name= input("enter your first_name ")
         l_name=input("enter your last name ")
         username=input("enter your username ")
         phone_number=int(input("enter your phone_number "))
         account_number = cls.generate_digits(12)
         account_type=input("enter your account type: savings/current/fixed ")
         account_balance=0
         pin=(input("enter your 5 digit pin"))
         # if len(pin) >= 5:
         #    print("your pin should not be greater than 5 numbers ")
         #    return
         # else:
         #    pin
         password=input("enter your password ")
         
         data= {
               "firstname": f_name,
               "lastname": l_name,
               "username": username,
               "phone_number": phone_number,
               "account_number": account_number,
               "account_type": account_type,
               "account_balance": account_balance,
               "pin":en_crypt(pin, 58),
               "password": en_crypt(password, 58)
         }
         
         if len(cls.customer_db("app.csv")) < 1:
            write.writeheader()
            write.writerow(data)
         else:
            write.writerow(data)
      

   def sign_in(self):
      for info in self.database:
         if info['username'] == self.username and decrypt(info['password'], 58) == self.password:
            print(decrypt(info['password'], 58))
            write_log_csv(self.username, f"{self.username} signed in" )
            return (f"you are welcome, {self.username}")
            

      else:
         print("Username does not match password")
         print("try again")
         

   def view_account_bal(self):
      for info in self.database:
         if self.username ==  info['username'] and self.password == decrypt(info['password'], 58):
            write_log_csv(self.username, f"viewed account balance" )
            print(f"Your account balance is N{int(info['account_balance']):,}")

   
   def withdraw_money(self):
      list_db=self.customer_db("app.csv")
      for i in range(len(list_db)):
         if self.username == list_db[i]['username'] and self.password == decrypt(list_db[i]['password'], 58):
            money_withdraw=int(input("how much do you want to withdraw? "))
            self.money_withdraw= money_withdraw
      
      for i in range(len(list_db)):
         if self.username == list_db[i]['username'] and self.password == decrypt(list_db[i]['password'], 58) and \
            int(list_db[i]['account_balance']) >= int(self.money_withdraw):
           
            x = int(list_db[i]['account_balance']) - int(self.money_withdraw)
            self.x=x

            df = pd.read_csv('app.csv')
            df.loc[list_db.index(list_db[i]), 'account_balance'] = self.x
            df.to_csv('app.csv', index=False)
            print(f"N{int(self.money_withdraw):,} has been withdrawn from your account")
            write_log_csv(self.username, f"{self.username} withdrew {self.money_withdraw}" )
         
         elif self.username == list_db[i]['username'] and self.password == decrypt(list_db[i]['password'], 58) and \
            int(list_db[i]['account_balance']) < int(self.money_withdraw):
            print("Insufficient fund")
   
   def customer_transfer(self, recipent_acct_no, amount):
      self.recipent_acct_no=recipent_acct_no
      self.amount=amount

      for info in self.database:
         if info['username'] == self.username and decrypt(info['password'], 58) == self.password:
            if int(info['account_balance']) < amount:
               return "Insufficient funds"
            y= int(info['account_balance']) - self.amount
            self.y=y

            df = pd.read_csv('app.csv')
            df.loc[self.database.index(info), 'account_balance'] = self.y
            df.to_csv('app.csv', index=False)
            write_log_csv(self.username, f"{self.username} tranferred {self.amount}" )

            # print(info['account_balance'])
            break
      else:
         return "Invalid account details"
      
      for record in self.database:
         # if record['account_number'] == recipent_acct_no:
         if self.recipent_acct_no in record.values():
            x=int(record['account_balance']) + self.amount
            self.x=x
            df = pd.read_csv('app.csv')
            df.loc[self.database.index(record), 'account_balance'] = self.x
            df.to_csv('app.csv', index=False)
            print(f"N{int(self.amount):,} was tranferred from you account to {record['username']}")
            write_log_csv(record['username'], f"{record['username']} received {self.amount}" )

            return(f"Your account balance is now N{(self.y):,}")
            

      info['account_balance'] += amount 
         
            
   def log_out(self):
      sys.exit()
                

class Staff(Admin):
   def staff_sign_in(self, username, password):
      list_staff=self.staff_db("staff_db.csv")
      
      # username=input("enter your username")
      # password=input("enter your password")
      
      for i in range(len(list_staff)):
         if list_staff[i]['change_password'] == ' ':
            # change_password1=input("enter a new password")
            change_password=input("change your password")
            self.change_password=change_password
            self.username=username
            self.password=password
            print(list_staff.index(list_staff[i]))
            df = pd.read_csv('staff_db.csv')
            df.loc[list_staff.index(list_staff[i]), 'change_password'] = self.change_password
            df.to_csv('staff_db.csv', index=False)
            write_stafflog_csv(f"{self.username}", "changed password" )
            list_staff=self.staff_db("staff_db.csv")


            if self.username == list_staff[i]['username'] and self.password == list_staff[i]['password'] and self.change_password == list_staff[i]['change_password']\
               and list_staff[i]["status"]== "is_active":
               return "you are welcome", self.username   #re-check
               
            elif self.username == list_staff[i]['username'] and list_staff[i]['change_password'] ==self.change_password\
               and list_staff[i]["status"]== "not_active":
               
               return("Your account has been deactivated")

            else:
               return("Username does not match password")
            
         else:
            self.username=username
            self.change_password=password
            if self.username == list_staff[i]['username'] and self.change_password == list_staff[i]['change_password']\
               and list_staff[i]["status"]== "is_active":
               write_stafflog_csv(f"{self.username} signed in" )
               return("you are welcome", self.username)

            elif self.username == list_staff[i]['username'] and self.change_password == list_staff[i]['change_password']\
               and list_staff[i]["status"]== "not_active":
               return("Your account has been deactivated")

      else:
         print("Username does not match password")
         print("try again")


   def staff_view_customer_bal(self):
      customer_name=input("enter the username of the customer")
      customer_acct_no=input("enter the account no of the customer")
      self.customer_name=customer_name
      self.customer_acct_no=customer_acct_no

      class_customer= Customer(read_csv('app.csv'), customer_name, customer_acct_no)
      list_db=class_customer.customer_db("app.csv")
      for i in range(len(list_db)):
         if list_db[i]['username'] == self.customer_name  and self.customer_acct_no == list_db[i]['account_number']: 
            # write_stafflog_csv(user_name.staff_sign_in(self.username), f"viewed {self.customer_name} account balance" )
            print(f"{self.customer_name}'s account balance is {list_db[i]['account_balance']}")
            break
         else:
            print("incorrect credentials")
            break
   
   def deposit_for_customer(self):
      
      customer_name=input("enter the username of the customer")
      deposit=int(input("How much do you want to deposit"))
      self.customer_name=customer_name
      self.deposit=deposit

      class_customer= Customer(read_csv('app.csv'), customer_name, deposit)
      list_db=class_customer.customer_db("app.csv")
      for i in range(len(list_db)):
         if self.customer_name in list_db[i]['username']: 
            y= int(list_db[i]['account_balance']) + self.deposit
            
            self.y=y
            df = pd.read_csv('app.csv')
            df.loc[list_db.index(list_db[i]), 'account_balance'] = self.y
            df.to_csv('app.csv', index=False)
            write_stafflog_csv(self.username, f"deposit for customer" )
            print(f"{(self.deposit):,} has been deposited {self.customer} account")
         
         

           
staff=Staff()
admin=Admin()
# admin.admin_create_account()
while True:
   print("Welcome to the Bank App.")
   print("How do you want to login?")
   print()
   print("1. ADMIN")
   print("2. STAFF")
   print("3. CUSTOMER")
   print("4. EXIT")
   print()
   choice = input("Enter your choice: \n")
   
   if choice == "1":
      print("______")
      print()
      print("Welcome Admin!")
      print("Please provide your login details")
      print()
      username=input("enter your username \n")
      print("______")
      password=input("enter your password \n")
      print("______")
      admin.sign_in(username, password)
      admin_db=read_csv("admin_db.csv")
      for i in range(len(admin_db)):
         if admin_db[i]['username'] == username and decrypt(admin_db[i]['password'], 58) == password:
            print("What would you like to do?")
            while True:
               print("1. Create staff\n2. View admin's activities\n3. View staffs' activities\n4. View customer's activities\
                     \n5. View customer's database\n6. View staff's database \
                     \n7. Suspend account\n8. Reactivate account\n9. Back\n00. Log out")
               admin_choice=input("Enter your choice: ")
               if admin_choice == "1":
                     admin=Admin()
                     admin.staff_create_account()
               elif admin_choice == "2":
                     print(read_csv('admin_activity_logs.csv'))
               elif admin_choice == "3":
                     print(read_csv('staff_activity_logs.csv'))
               elif admin_choice == "4":
                     print(read_csv('customer_activity_logs.csv'))
               elif admin_choice == "5":
                     print(read_csv('app.csv'))
               elif admin_choice == "6":
                     print(read_csv('staff_db.csv'))
               elif admin_choice == "7":
                     admin.suspend_staff_account()
               elif admin_choice == "8":
                     admin.reactivate_staff_account()
               elif choice == "9":
                  while True:
                     if choice == "9":
                        break
               elif admin_choice == "00":
                     admin.log_out()   #for exit
               else:
                     print("Invalid input, please try again")
         
   elif choice == "2":

      print("You are welcome.")
      print("Please provide your login details")
      print()
      username=input("enter your username")
      password=input("enter your password")
      staff.staff_sign_in(username, password)
      list_staff=read_csv("staff_db.csv")
      for i in range(len(list_staff)):
         if list_staff[i]['username'] == username and list_staff[i]['change_password'] == password and\
         list_staff[i]['status'] == "not_active":
            print("Your account has been suspended")
            print()
         elif list_staff[i]['username'] == username and list_staff[i]['change_password'] == password:
            print(f"You are welcome {username}")
            print("What would you like to do?")    
            while True:
               
               print("1. View Customer's balance\n2. Deposit for customer\n3. Back\n4. Log out") 

               staff_action=input("Enter your choice. ")
               if staff_action == "1":
                  print(staff.staff_view_customer_bal())
               elif staff_action == "2":
                  print(staff.deposit_for_customer())
               elif staff_action == "3":
                  while True:
                     if staff_action == "3":
                        break
               elif staff_action == "4":
                  staff.log_out()
                  #for exit

               else:
                  print("Invalid input please try again")
         
         

         # else:
         #    print("Username does not match password!!!") 
         #    break  
   elif choice == "3":
      
      while True:
         print("You are welcome our esteemed customer.")
         print("Welcome to Bank app!")
         print("1. Create account")
         print("2. Login")
         print("3. Exit")
         print("What transactions would you like to perform?")
         
         cust_choice = input("enter your choice")
         if cust_choice == "1":

           
      
            Customer.customer_create_account()
            print("please provide your login details below\n")
            username=input("enter username")
            password=input("enter password")
            customer=Customer(read_csv('app.csv'), username, password)
            customer1=read_csv('app.csv')

            print(customer.sign_in())
            for i in range(len(customer1)):
               if customer1[i]['username'] == username and decrypt(customer1[i]['password'], 58) == password:
                  print("\nWhat would you like to do?")
                  print()
                  while True:
                     print("1. View account balance\n2. Withdraw\n3. Transfer\n4. Back\n5. Log out") 

                     customer_action=input("Enter your choice. ")
                     if customer_action == "1":
                           customer.view_account_bal()
                     elif customer_action == "2":
                           customer.withdraw_money()
                     elif customer_action == "3":
                           recipent_acct_no=input("Enter the recipent account number. ")
                           amount=int(input("Enter the amount you want to transfer "))
                           print(customer.customer_transfer(recipent_acct_no, amount))
                     elif customer_action == "4":
                           while True:
                              if customer_action == "4":
                                 break
                     elif customer_action == "5":
                           break #for exit

                     else:
                           print("Invalid input please try again")
                  
         elif cust_choice == "2":
            username=input("enter username")
            password=input("enter password")
            customer=Customer(read_csv('app.csv'), username, password)
            customer1=read_csv('app.csv')

            print(customer.sign_in())
            for i in range(len(customer1)):
               if customer1[i]['username'] == username and decrypt(customer1[i]['password'], 58) == password:
                  print("\nWhat would you like to do?")
                  print()
                  while True:

                     print("1. View account balance\n2. Withdraw\n3. Transfer\n4. Back\n5. Log out") 

                     customer_action=input("Enter your choice. ")
                     if customer_action == "1":
                           customer.view_account_bal()
                     elif customer_action == "2":
                           customer.withdraw_money()
                     elif customer_action == "3":
                           recipent_acct_no=input("Enter the recipent account number. ")
                           amount=int(input("Enter the amount you want to transfer "))
                           print(customer.customer_transfer(recipent_acct_no, amount))
                     elif customer_action == "4":
                           while True:
                              if customer_action == "4":
                                 break
                     elif customer_action == "5":
                           customer.log_out() #for exit

                     else:
                           print("Invalid input please try again")
         elif cust_choice == "3":
            sys.exit()
   elif choice== "4":
      admin.log_out()
      
   else:
      print("Invalid choice. Please try again.")




