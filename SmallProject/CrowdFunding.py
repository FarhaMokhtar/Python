import json
import os
import re
from datetime import datetime

#DataBase (json files pathes)
USERS="SmallProject/mydata/user.json"
PROJECTS="SmallProject/mydata/projects.json"

#Hellper Functions ...... 
def Read_From_File(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  


def Write_Into_File(file , data):
    with open(file, "w") as f: 
        json.dump(data, f, indent=4)  




#Registeration function ......

def register ():
     users= Read_From_File(USERS)
     print("\n===== Register =====")
     FirstName= input("Hi ! Please Enter Your First Name : ")
     LastName= input("Now ! Enter your Last Name : ")
     Email=input("Please ! Enter your Email : ")

     #validation email format ...
     if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$" , Email):
        print("\n⚠ Invalid Email Format,it must be like that :local@domain.com ,please try again !")    
        return 
     #check if user is already exists
     if any(user["email"] == Email for user in users):
        print("\n⚠ Email already exists! Try logging in.")
        return
     
     Password = input("thanks! PLease now Enter Your secrit Password : ")
     Confirm_Password= input("please , Enter the Confirm Password : ")
     #validate confirm password
     if Password != Confirm_Password:
          print("\n⚠ Confirm Password must be match your password, please try again !")
          return
     Phone=input("please Enter Your Phone Number : ")
     #validation Egyption Phone number 
     if not re.match(r"^01[0-2,5]\d{8}$", Phone):
          print("\n⚠ Invalid Egyptian phone number!")
          return
     
     
     users.append({"first_name": FirstName, "last_name": LastName, "email": Email, "password": Password, "phone": Phone})   
     Write_Into_File(USERS , users)
     print("\n✅ Congrats ,Registration successful! You can now log in.")


#Login function ......
def Login():
    users= Read_From_File(USERS)
    print("\n===== Login =====")

    Email= input("Please Enter Ur Email : ")
    Password=input("Please Enter Ur Paasword : ")
    if any(user["email"] == Email and user["password"]== Password for user in users):
      print("\n✅ Congrats ,Login successful! You can now log in.")
      return Email
    else:
       print("\n⚠ Ur Password or Ur Email is not correct ! Please try again ...")   
       return

##################################################
#create project
def Create_Project(Email):
    projects=Read_From_File(PROJECTS)
    print("\n===== Create Project =====")

    Title= input("Please Enter Project Title : ")
    Details= input("Please Enter Project Details :")
    Total_Target = input("Please Enter Target Amount (EGP) : ")
    start_date=input("Enter start date (YYYY-MM-DD): ")
    end_date= input("Enter end date (YYYY-MM-DD): ")

    try:
      start_date= datetime.strptime(start_date , "%Y-%m-%d")
      end_date = datetime.strptime(end_date ,"%Y-%m-%d" )
      if start_date >= end_date :
        print("\n⚠ End date must be after start date!")
        return
    except :
        print("\n⚠ Invalid date format!")
        return

    projects.append({"title":Title , "details":Details , "target":Total_Target , "start_date":str(start_date.date()) , "end_date":str(end_date.date()) , "owner_project":Email})   
    Write_Into_File(PROJECTS , projects)
    print("\n✅ Project created successfully! Thank You ....")



#View All Projects 
def View_All_Projects():
    projects=Read_From_File(PROJECTS)
    print("\n===== Projects List =====")

    if not projects:
        print("\n⚠ No Projects Found!")
    else:    
        for p in projects :
            print(f"\n📌 Title: {p['title']}\n📄 Details: {p['details']}\n💰 Target: {p['target']} EGP\n📅 Start Date: {p['start_date']}\n📅 End Date: {p['end_date']}\n👤 Owner: {p['owner_project']}")


#Edit his own project
def edit_project(Email):
    projects = Read_From_File(PROJECTS)
    print("\n===== Edit Project =====")

    title = input("Enter project title to edit: ")
    
    for p in projects:
        if p["title"] == title and p["owner_project"] == Email:
            print("\nWhat would you like to edit?")
            while True:
                print("1. Title\n2. Details\n3. Target\n4. Start Date\n5. End Date\n6. Exit Editing")
                choice = input("Your choice: ")

                if choice == "1":
                    p["title"] = input("Enter new title: ")
                elif choice == "2":
                    p["details"] = input("Enter new details: ")
                elif choice == "3":
                    p["target"] = float(input("Enter new target amount (EGP): "))
                elif choice == "4":
                    new_start_date = input("Enter new start date (YYYY-MM-DD): ")
                    try:
                        new_start_date = datetime.strptime(new_start_date, "%Y-%m-%d").date()
                        if new_start_date >= datetime.strptime(p["end_date"], "%Y-%m-%d").date():
                            print("\n⚠ Start date must be before the end date!")
                        else:
                            p["start_date"] = str(new_start_date)
                    except ValueError:
                        print("Invalid date format!")
                elif choice == "5":
                    new_end_date = input("Enter new end date (YYYY-MM-DD): ")
                    try:
                        new_end_date = datetime.strptime(new_end_date, "%Y-%m-%d").date()
                        if new_end_date <= datetime.strptime(p["start_date"], "%Y-%m-%d").date():
                            print("\n⚠ End date must be after the start date!")
                        else:
                            p["end_date"] = str(new_end_date)
                    except ValueError:
                        print("\n⚠ Invalid date format!")
                elif choice == "6":
                    print("\n✅ Project updated successfully!")
                    Write_Into_File(PROJECTS, projects)
                    return
                else:
                    print("\n⚠ Invalid choice! Please select a valid option.")

    print("\n⚠ Project not found or unauthorized access!")


#Remove his own project
def remove_project(Email):
        projects = Read_From_File(PROJECTS)
        print("\n===== Delete Project =====")
        Title = input("Please Enter project Title to Remove it : ")
        for project in projects:
            if project["owner_project"]==Email and project["title"]==Title:
                projects.remove(project)
                Write_Into_File(PROJECTS, projects)
                print("\n✅ Project deleted successfully!")
                return
        else:
            print("\n⚠ Not Found That ... ")    

#Search for project by date 
def Search_by_Date():
    projects = Read_From_File(PROJECTS)
    print("\n===== Search Projects by Date =====")

    date = input("Enter date to search (YYYY-MM-DD): ")
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        results = [p for p in projects if datetime.strptime(p["start_date"], "%Y-%m-%d").date() <= date <= datetime.strptime(p["end_date"], "%Y-%m-%d").date()]
        if results:
            for p in results:
                print(f"\n📌 Title: {p['title']}\n📄 Details: {p['details']}\n💰 Target: {p['target']} EGP\n📅 Start Date: {p['start_date']}\n📅 End Date: {p['end_date']}\n👤 Owner: {p['owner_project']}")
        else:
            print("\n⚠ No projects found for this date.")
    except ValueError:
        print("\n⚠ Invalid date format!")

#main 

def main ():
    while True :
        print("\n===== Main Menu =====")
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Please Enter your choice : ")
        if choice =="1":
            register()
        elif choice == "2":
          email= Login()
          if email :
              while True:
                    print("\n1. Create Project\n2. View Projects\n3. Edit Project\n4. Delete Project\n5. Search Projects by Date\n6. Logout")
                    option = input("Choose an option: ")
                    if option == "1":
                        Create_Project(email)
                    if option == "2":
                        View_All_Projects()
                    if option == "3":
                        edit_project(email)
                    if option == "4":
                        remove_project(email)
                    if option =="5" :
                        Search_by_Date()
                    if option =="6":
                        break
        elif choice == "3":
            print("\n👋 Goodbye!")
            break
  
main()
                









    


