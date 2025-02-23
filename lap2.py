import re
#Question 1 :
# Write a simple calculator program using match to perform addition, subtraction, multiplication, and division.
# operation = "add"
# a, b = 10, 5
print("##"*10 +" Question 1 "+ "##"*10)

operation = input("Please Enter operation name : ")
num1= int(input("Now! please enter number 1 :"))
num2= int(input("Now! please enter number 2 :"))

match operation:
    case "add":
        print(num1+num2)
    case "sub":
        print(num1-num2)
    case "multi":
        print(num1*num2)
    case "div":
        print(num1/num2)
    case _:
        print("Please Enter Valide Operation .")    


#Question 2 :
# Write a program to filter out even numbers from a list and count how many are left.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("##"*10 +" Question 2 "+ "##"*10)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filterdnums=[]
for num in numbers:
    if num %2 !=0 :
        filterdnums.append(num)

print(filterdnums)
print(len(filterdnums))      

#Question 3 :
# Write a program to check if a password meets the following criteria:
# - At least 8 characters long.
# - Contains at least one uppercase letter.
# - Contains at least one digit.
# password = "Pass1234"
print("##"*10 +" Question 3 "+ "##"*10)
password = input("please Enter ur password : ")
len8 = len(password) >= 8
isupper = False
isdigit = False

for i in password:
    if (i.isupper()):
        isupper=True
    if(i.isdigit()):
        isdigit= True

if not len8:
    print("Password must be at least 8 characters long!")
if not isupper:
    print("Password must contain at least one uppercase letter!")
if not isdigit:
    print("Password must contain at least one digit!")
            
if len8 and isdigit and isupper    :
    print("Valid Password ! than you ....")

     
# Question 4: 
# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :

print("##"*10+" Question 4 "+ "##"*10)

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4=dict( dic1 | dic2 |dic3)
print(dic4)
print(type(dic4))

# Question 5: 
# takes a string and prints the longest
# alphabetical ordered substring occured.
# For example, if the string is 'abdulrahman' then the output is:
# Longest substring in alphabetical order is: abdu

print("##"*10+" Question 5 "+ "##"*10)

string = input("Please Enter a string : ")
longest=""
current = string[0]

for i in range(1 ,len(string)):
    if string[i] >= string[i-1]:
        current+=string[i]
    else:   
        if len(current)> len(longest):
            longest=current
        current=string[i]

if len(current) >len(longest):
    longest= current

print("ongest substring in alphabetical order is : %s" %longest )    


# Question 6:
# Write a program to check if a Email meets the following criteria:
# - Ensures the email follows a standard format (e.g., local@domain.com).
# - Does not check if the email actually exists or is deliverable.
print("##"*10+" Question 6 "+ "##"*10)
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$'
email= input("Please Enter ur Email : ")

if re.match(pattern , email):
    print("valid email! thank you ...")
else:
    print("Invalid email , please try again ! it must be like that :local@domain.com")    








