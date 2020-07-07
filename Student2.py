
from os import system, name
from time import sleep
from datetime import datetime
import re


class Student(object):
    """
    Student class with attribute
    rollno type int
    PRN_No type int
    Name type string
    DOB type int
    Email type string
    Contact type int
    """

    no_of_Student = 0


    def __init__(self, rollno, prnno, name, DOB, email_id, contact):
        
        self.rollno = rollno
        self.prnno = prnno
        self.name = name
        self.DOB = DOB
        self.email_id = email_id
        self.contact = contact
        


    @property
    def rollno(self):
        return self.__rollno

    @rollno.setter
    def rollno(self, rollno):
        while True:
            pattern = "[1-9]+$"
            rollnoMatch = re.match(pattern,rollno)
            if rollnoMatch:
                self.__rollno = rollno
                break
            else:
                print("Invalid rollno !!")
                rollno = raw_input("Enter your RollNo: ")

                continue


    @property
    def prnno(self):
        return self.__prnno

    @prnno.setter
    def prnno(self, prnno):
        while True:
            pattern = "[022018]+[0-9]+$"
            prnnoMatch = re.match(pattern,prnno)
            if prnnoMatch :
                self.__prnno = prnno
                break
            else:
                print("Invalid prn number")
                prnno = raw_input("Enter your PRN_No: ")
                continue

    

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        while True:
            if name.isalpha():
                self.__name = name
                break
            else:
                print("Invalid name")
                name = raw_input("Enter your name: ")
                continue

    @property
    def DOB(self):
        return self.__DOB

    @DOB.setter
    def DOB(self, DOB):
        while True:
            try:
                dt_start = datetime.strptime(DOB, '%d/%m/%Y')
                self.__DOB = DOB
                break
            except ValueError:
                print "Incorrect format"
                DOB = str(raw_input("Enter your date of birth in the format DD/MM/YYYY: "))
                continue
            
        
    
    @property
    def email_id(self):
        return self.__email_id

    @email_id.setter
    def email_id(self, email_id):
        while True:
            pattern = "^[A-Za-z0-9]+\@[A-Za-z0-9]+\.[A-Za-z0-9]+$"
            email_idMatch = re.match(pattern,email_id)
            if email_idMatch:
                self.__email_id = email_id
                break
            else:
                print ("Invalid email id")
                email_id = raw_input("Enter your Email ID: ")
                continue


    @property
    def contact(self):
        return self.__contact

    @contact.setter
    def contact(self, contact):
        while True:
            pattern = re.compile("(0/91)?[7-9][0-9]{9}")
            if pattern.match(contact):
                self.__contact = contact
                print ("Student record added successfully !!!")
                break
            else:
                print("Invalid contact No")
                contact = raw_input("Enter your Contact No: ")
                continue


class Studdemo(object):

    stud_list = {}
    last_studid = 0

    
    
    @staticmethod
    def addStudent():

        Studdemo.last_studid += 1
        studid = Studdemo.last_studid
        rollno = raw_input("Enter your RollNo: ")
        prnno = raw_input("Enter your PRN_No: ")
        name = raw_input("Enter your name: ")
        DOB = str(raw_input("Enter your date of birth in the format DD/MM/YYYY: "))
        email_id = raw_input("Enter your Email ID: ")
        contact = raw_input("Enter the contact no:")
        

        Studdemo.stud_list[studid] = Student(rollno,prnno,name,DOB,email_id,contact)
             
        
        
    @staticmethod
    def delete():
        rollno = raw_input("Enter the rollno that you want to delete:")
        for id,s in Studdemo.stud_list.iteritems():
            if s.rollno == rollno:
                Studdemo.stud_list.clear()
                print ("Record deleted")
                break
            else:
                print("Already deleted or record not found")
        
        
        print "Rollno\tPRN_No\tName\tDOB\tEmail_id\tcontact"
        for id,s in Studdemo.stud_list.iteritems():
            print id,"\t\t",s.rollno, "\t" , s.prnno, "\t" ,s.name,"\t",s.DOB, "\t" , s.email_id, "\t" ,s.contact




    @staticmethod
    def search():
        prnno = raw_input("Enter the prnno for search:")
        for id,s in Studdemo.stud_list.iteritems():
            if s.prnno == prnno:
                for id,s in Studdemo.stud_list.iteritems():
                    print id,"\t\t",s.rollno, "\t" , s.prnno, "\t" ,s.name,"\t",s.DOB, "\t" , s.email_id, "\t" ,s.contact

                print("record found in list")
                break
            else:
                
                print("record not found")

   

    @staticmethod
    def update():
        print("Enter the prn no of student for updation !!!")
        prnno = raw_input("Enter the prnno for search:")
        for id,s in Studdemo.stud_list.iteritems():
            if s.prnno == prnno:
                print("record found in list")
                for id,s in Studdemo.stud_list.iteritems():
                    if s.prnno == prnno:
                        Studdemo.stud_list.clear()
                        break
                print("Enter the data !!")
                Studdemo.addStudent()
                print("Updation completed")
               
                break
            else:
                
                print("record not found")








    @staticmethod
    def display():

        
        print "Rollno\tPRN_No\tName\tDOB\tEmail_id\tcontact"
        for id,s in Studdemo.stud_list.iteritems():
            print id,"\t\t",s.rollno, "\t" , s.prnno, "\t" ,s.name,"\t",s.DOB, "\t" , s.email_id, "\t" ,s.contact
        

        
        
        
        
                    
        
                    


def clear():
    if name == "nt":
        _ = system("cls")
    
    else:
        _ = system("clear")


        

