import math
import re
print("___________________q1_________________________")

#q1
# Remove the first occurance of 20
a = [10, 20, 30, 20, 40, 50]
for i in range(len(a)):
    if a[i] == 20:
        del a[i]
        break
print(a)
print("___________________q2_________________________")

#q2
# Remove element at index 1 and return its value in val
var=a.pop(1)
print(var)
print(a)
print("___________________q3_________________________")

#q3
# Removes elements from index 1 to index 3 (which are 20, 30, 40)
x = [10, 20, 30, 40, 50, 60, 70]
del x[1:3]
print(x)
print("___________________q4_________________________")

#q4
# Remove all elements
y= [10, 20, 30, 40, 50, 60, 70]
del y[::]
print(y)
print("___________________q5_________________________")

#q5
# Write a program that prints the number of times the substring 'iti' occurs in a string
string ='iti'
countI= string.lower().count('i')
print(countI)
print("___________________q6_________________________")

#q6
# application to take a number in binary form from the user, and print it as a decimal
binary = input("Please Enter your Binary Num!")
if binary.count('0')+binary.count('1') ==len(binary):
    dicimal = int(binary,2)
    print("decimal unm is : %d" %dicimal)
else :
    print("Error")

print("___________________q7_________________________")

#q7
# write a code take a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is divisible by both return "FizzBuzz"
num = int(input("please enter your num :"))

if num%5 == 0 and num%3==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("buzz")
else:
    print("Errorrrr!!!")
print("___________________q8_________________________")


#q8
# Ask the user to enter the radius of a circle print its calculated area and circumference
radius=float( input("Please Enter radius : "))
Area=round(math.pi * radius**2,2)
print("Area f circle is : %d" %Area)
circumference =round(math.pi * 2* radius)
print("circumference f circle is : %d" %circumference)
print("___________________q9_________________________")

#q9
# Ask the user for his name then confirm that he has entered his name (not an empty string/integers).then proceed to ask him for his email and print all this data
name= input("Please Enter Your Name : ")
email = input("Please Enter ur Email : ")
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

if len(name) != 0 and name.isalpha(): 
    print("%s  name is valid " %name)
else:
    print("Invalid name! Please enter a valid name (letters only).")    

if re.match(pattern , email):
    print("%s  email is valid " %email)
else:
    print("Invalid email format! Please enter a valid email (e.g., example@example.com).")        














