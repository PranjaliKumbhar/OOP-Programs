from Student2 import *
from os import system, name
from time import sleep
from datetime import datetime
import re


def main():

    
    s1 = Studdemo()
    clear()

    print ("*"*50)
    print ("Welcome to menu driven program")
    print ("*"*50)

    sleep(2)

    while True:

        print ("-"*50)
        print ("1.Add a new student")
        print ("2.Delete student by rollno")
        print ("3.Search student by prnno")
        print ("4.Update the student information")
        print ("5.Display or list the all students")
        print ("6.Exit")

        choice = input("Enter your choice: ")
       
        

        if choice == 1:
            s1.addStudent()
        
        elif choice == 2:
            s1.delete()
        
        elif choice == 3:
            s1.search()
        
        elif choice == 4:
            s1.update()
        
        elif choice == 5:
            s1.display()
           
        elif choice == 6:
            print ("Thank you !!")
            break
        
        else:
            print ("entered choice is invalid")


if __name__ == '__main__':
    main()
