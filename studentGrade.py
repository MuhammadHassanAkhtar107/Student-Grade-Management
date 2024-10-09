studentdata={ }

def addstudent(name,grade):
    studentdata[name]=grade
    print(f"{name} grade is {grade}")
def updatestudent(name,grade):
    if name in studentdata:
        studentdata[name]=grade
        print(f"{name} update with data with its grade {grade}")
    else:
        print(f"{name} is not found")
def delstudent(name):
    if name in studentdata:
        del studentdata[name]
        print(f"{name} is deleted")
    else:
        print(f"{name} not found")

def view():
    while True:
        print("Student Grade Managment system")
        print("1. Add Student \n2. Update Student \n3. Delete Student \n4. View Data \n5. Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            name=input("Enter Student Name:")
            grade=int(input("Enter Student Number:"))
            addstudent(name,grade)
        elif choice==2:
            name=input("Enter Student Name:")
            grade=int(input("Enter Student Number:"))
            updatestudent(name,grade)
        elif choice==3:
            name=input("Enter Student Name:")
            delstudent(name)
        elif choice==4:
            print(studentdata)
        elif choice==5:
            print("-----Ended-----")
            break
        else:
            print("Chuz valid number")
view()






























# studentdata={ }

# def addstudent(name,grade):
#     studentdata[name]=grade
#     print(f"Add {name} with a {grade}")
# def updatestudent(name,grade):
#     if name in studentdata:
#         studentdata[name]=grade
#         print(f"{name} with marks are updated {grade}")
# def delstudent(name):
#     if name in studentdata:
#         del studentdata[name]
#         print(f"{name} is deleted")
#     else:
#         print(f"{name} is not found")
# def viewstudentdata():
#     if studentdata:
#         for name,grade in studentdata.items():
#             print(f"{name}:{grade}")
#         else:
#             print("no student found")

# def main():
#     while True:
#         print("Student Grades Management System")
#         print("1. Add Student \n2. Update Student \n3. Delete Student \n4. View Student \n5. Exit")
#         choice=int(input("Enter your choice: "))

#         if choice==1:
#             studentname=input("Enter Student Name:")
#             studentnumber=int(input("Enter Student Number:"))
#             addstudent(studentname,studentnumber)
#         elif choice==2:
#             studentname=input("Enter Student Name:")
#             studentnumber=int(input("Enter Student Number:"))
#             updatestudent(studentname,studentnumber)
#         elif choice==3:
#             studentname=input("Enter Student Name:")
#             delstudent(studentname)
#         elif choice==4:
#             print(studentdata)
#         elif choice==5:
#             print("-----Ending-----5")
#             break
# main()