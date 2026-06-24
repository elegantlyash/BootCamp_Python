#date : 8.06.2007
'''
#WAP to perform calculation on two number
o = input('enter Operation "+", "-","/","*" :')
a = int(input("Enter number a "))
b = int(input("Enter number b "))
if o =="+":
    print("Addition of two numbers is",a+b)
elif o =="-":
    print("Subtraction of two numbers is",a-b)
elif o =="/":
    print("Division of two numbers is",a/b)
elif o =="*":
    print("Multiplication of two numbers is",a*b)

#WAP to find the salary of an employee
num = int(input("enter number of employees"))
for i in range(num) :
    def salary():
        store = []

        Emp_id = int(input("Enter Employee ID : "))
        name = input("Enter Employee Name : ")
        Basic_salary = int(input("Enter Salary : "))

        hra = 0.2*Basic_salary
        da = 0.15*Basic_salary
        tax = 0.1*Basic_salary

        gross_salary = Basic_salary + hra + da + tax
        net_salary =  gross_salary - (hra + da + tax)

        print(f"Gross Salary of {name} is {gross_salary}")
        print(f"Net Salary of {name} is {net_salary}")
        
        store.append(Emp_id)
        store.append(name)
        store.append(gross_salary)
        store.append(net_salary)

        print(f"Data of {name} is : {store}")
    salary()

#WAP of simple ATM
print("Welcome to ATM")
print("1. Check Balance")
print("2. Withdraw Money")    
print("3. Deposit Money")
print("4. Transaction History")
print("5. Exit") 
balance = 1000
while True:
    choice = int(input('Enter your choice '))
    
    if choice == 1 :
        print("Available Balance, ",balance)
        
    elif choice == 2:
        withdraw_amt = int(input('Enter amount to withdraw '))
        if withdraw_amt > balance:
                           print('Insufficient Balance')
        else:
            c_balance = balance - withdraw_amt
            print(f"{withdraw_amt} is deducted from {balance}, your Current Balance is {c_balance}")
            
    elif choice == 3:
        deposit_amt = int(input('Enter amount to deposit '))
        c_balance+=deposit_amt
        print(f"{deposit_amt} is deposited to {c_balance}, your Current Balance is {c_balance}")
        
    elif choice== 4:
        list=[]
        list.append(withdraw_amt)
        print("transaction history",list)
        
    else:
        print("thanks for visiting")
        break


#---- define a function----------
def greet(name, greeting='hello'):   #default arg
    """Return a greeting string"""
    return f"{greeting},{name}!"

#---- Call a function------------
msg = greet('Alice')
print(msg)  #hello Alice
print(greet("Bob","Hi")) #Hi, Bob!

#Lambda function
square = lambda x:x**2
add = lambda a,b : a+b

#Date : 10.06.2026
#wap unit convertor
print("Enter ln for lenth convertor")
print("Enter wh for weight convertor")
ch = input('Enter convertor type : ')
if ch == "ln":
        cm = int(input('enter your value in "cm" : '))
        print(f"km value of {cm} is ", cm*(0.00001))
        print(f"mm value of {cm} is ", cm*10)
        print(f"m value of {cm} is ", cm*(0.01))

elif ch == "wh":
        w = int(input('enter your value in "gram" : '))
        print(f"kg value of {w} is ", w*(0.001))
        print(f"mg value of {w} is ", w*1000)
        print(f"pound value of {w} is ", w*(0.00022))
else:
        print("ERROR : enter valid convertor type")

#wap to check wheather number is positive, negative or zero 
for i in range(5):
    num = int(input("Enter a number : "))
    if num > 0:
        print(f"{num} is positive.")
    elif num < 0:
        print(f"{num} is negative.")
    elif num ==0:
        print(f"{num} is zero.")
    else:
        print("ERROR : enter Valid number")

#wap to check wheather the year is leap year or not
yr = int(input("Enter year"))
if yr%4==0 and yr%400==0:
    print(f"{yr} is a leap year")
else :
    print(f"{yr} is not a leap year")


#wap Atm machine
print("--------Welcome----------")
pin = input("enter pin : ")
if pin == "1234":
    cr = int(input("Correct pin ! please enter the amount to withdraw : "))
    if cr <= 5000 :
        print(f"{cr} amount dispensing cash")
    else:
        print("Limit Exceeded")
else :
    print("Wrong pin , enter correct pin")
    

#Temperature advisor program
t = float(input("Enter Temperature in celcius : "))
if t < 0:
    print("Wear Heavy clothes")
elif t>=0 and t<=15:
    print("Wear a Jacket")
elif t>=16 and t<=30:
    print("Comfortable weather")
elif t>30:
    print("light clothes and stay hydrated")
else:
    print(f"{t} is invalid")

#Loan Eligibility Checker
i = int(input("Enter your monthly income : "))
p = float(input("Existing EMI  : "))
if i >=30000 and p<0.4*i:
    print("Eligible for loan")
elif i < 30000:
    print("Income too low")
elif p>0.4*i:
    print("High debt burden")
else:
    print("Error")

#Number guess program
while True:
    i = int(input("Guess the number : "))
    if 42<i:
        print("Too high")
    elif i<10:
        print("Too low")
    elif i<42:
        print("Low(may be near)")
    elif i==42:
        print("correct number ")
        break
    else:
        print("Wrong number")

#wap student's performance
e = float(input("Enter your marks : "))
if e>=40:
    print("pass")
    if e>=90 :
        print("Distinction")
    elif e >=75:
        print("First Division")
    elif e >= 60:
        print("Second Division")
    else:
        print("Third Division")
else:
    print("Fail")
#wap job application screener
age = int(input("Enter your age : "))
deg = input("Enter your degree (use . at appropriately): ").lower()
c = float(input("Enter your cgpa : "))
if 21<=age<=40 and deg == "b.tech" or deg == "mca" and c>=7:
    print("You are shortlisted for interview")
else:
    print("You did not qualify the eligibility criteria")

#wap e-commerce discount calculation
total = int(input("Enter your total amount : "))
p = input("Are you a premium user (y/n) : ").lower() 
if total>5000:
    print(f"15% discount applied on {total} you now have to pay",total*0.15)
    if p == 'y':
        print(f"20 % discount applied on {total} you now have to pay",total*0.2)
elif total <=5000:
    print(f"5% discount applied on {total} you now have to pay",total*0.05)
else:
    print("No discount")
    

def grade(m,max_marks=100):
    print(f"You scored {m}/{max_marks}")
    percentage = (m/max_marks)*100
    print(f"percentage : {percentage:.2f}")
    
    if 90<=m<=100:
        grade,cgpa,remarks="A+",10,"Exceptional"
    elif 80<=m<=89:
        grade,cgpa,remarks="A",9,"Excellent"
    elif 70<=m<=79:
        grade,cgpa,remarks="B+",8,"Very Good"
    elif 60<=m<=69:
        grade,cgpa,remarks="B",7,"Good"
    elif 50<=m<=59:
        grade,cgpa,remarks="C",6,"Avaerage"
    else:
        grade,cgpa,remarks="D",4,"Fail"

    print(f"Your Score : grade {grade},cgpa {cgpa} and your performance is {remarks}.")
m = int(input("Enter your marks : "))
grade(m)

#Date : 15.06.2026
#wap to find max of two number
a = int(input("Enter number : "))
b = int(input("Enter number: "))
if a>b:
        print(f"{a} is greater than {b}")
else :
        print(f"{b} is greater than {a}")

#wap to add number
N = int(input("Enter number : "))
if N%2!=0:
        N+=7
        print(N)
else:
        N+=4
        print(N)
        
#wap guessing game
while True:
    i = int(input("Guess the number : "))
    if 42<i:
        print("Too high")
    elif i<10:
        print("Too low")
    elif i<42:
        print("Low(may be near)")
    elif i==42:
        print("correct number ")
        break
    else:
        print("Wrong number")

#to find given number is + or -
n = 5
if n >=0:
        if n==0:
                print("Number is 0")
        else:
                print("Number is +")
else:
        print("Number is -")

#to find max among 3
a = int(input("Enter number a : "))
b = int(input("Enter number b : "))
c = int(input("Enter number c : "))
if (a>b):
        if (a>c):
                print("a is max")
        else:
                print("c is max")
else:
        if(b>c):
                print("B is max")
        else:
                print("C is max")

#wap to check wheather the number is +,- or 0 if + check if it's even or odd
num = int(input("Enter a number : "))
if num > 0:
        print(f"{num} is positive.")
        if num%2==0:
                print(f"{num} is even")
        else:
                print(f"{num} is odd")
elif num < 0:
        print(f"{num} is negative.")
elif num ==0:
        print(f"{num} is zero.")
else:
        print("ERROR : enter Valid number")

#wap to create grading system
s = int(input("Enter your grade : "))
if 90<=s<=100:
        print("Your grade is A")
elif 80<=s<=89:
        print("Your grade is B")
elif 70<=s<=79:
        print("Your grade is C")
elif 60<=s<=69:
        print("Your grade is D")
elif 0<=s<=59:
        print("Your grade is F")
else:
        print("ERROR enter a valid grade")


#wap to print table upto 10
for i in range(1,11):
        for j in range(1,11):
                print(i*j,end=" ")
        print()
                        

#print each number sqaured
l = [1,2,3,4,5,6,7,8,9,10]
for i in l:
        print(i**2,end=" ")

        
#print sum of all odd numbers
t = 0
n = 1
while n <= 50:
        t += n
        n += 2

print(t)

#wap to skip multiple of 7 from 1 to 50
for i in range(1,51):
        if i%7==0:
                continue
        else:
                print(i,end=" ")

#wap to add number entered by user
u = input("Enter numbers separated by commas: ").split(",")
sum = 0
for item in u:
    num = int(item.strip())
    
    if num % 2 == 0:
        sum = sum+num
print("The sum of even numbers is:", sum)


#wap to generate 
import random as rn
i = 0
count = 0
while i == 0:
    x = rn.randint(1,10)
    count+=1
    if x > 7:
        print(x,"is the number generated ")
        print("7 is reached")
        break
print(f"{count} number where generated")
    

#recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
print("factorial of 5:",factorial(5))

#Celcius to fehrenhiet
def temp(c):
    return(c*9/5)+32
print(temp(0))

#create a list multiplicative product of all values
l = [1,2,3,4,5]
t = 1
for i in l:
    t*=i
print(t)

#wap of palindrome text
def pal(a):
    if a==a[::-1]:
        print("Text is palindrome")
    else:
        print(f"{a} is not palindrome")
pal(a = input("Enter text to check : ").lower())
#wap to fibonaci

a, b = 0, 1
n = int(input("Enter number of terms : "))
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
#Date : 17.06.26

#wap library fine calculator

i=0
t=0
m= 0

while True:
    
    print("enter break to end")
    s = input("Enter your name : ")
    
    if s.lower()=="break":
        print("End")
        break
    
    d = int(input("Enter days late  : "))   
    if 1<=d<=5:
        amt=d*5
        print("5 ruppee per day charged")
    elif 6<=d<=10:
        amt=d*10
        print("10 Ruppee per day charged")
    elif d>10:
        amt=d*20
        print("20 Ruppee per day charged")
    if m < amt:
        m += amt
        
    i+=1
    t+=amt
    
    print(f" Amount paid by {s} is ",amt)
    print(f"Total amount collected is {t}")
    print("Average of fine is ",t/i) 
    print("Max fine is ",m)

def student_report(name,marks):
    print("Name : ",name)
    print("Marks : ",marks)
name=input("Enter Student name: ")
marks=int(input("Enter Marks: "))
student_report(name,marks)

def add_bonus(marks):
    print("Inside Function Marks",marks+5)
add_bonus(marks)
print("Outside function marks",marks)


def sum_marks(n):
    if n <= 0:
        return 0
    else:
        return n + sum_marks(n - 1)

num = int(input("Enter a number for recursive sum: "))
result = sum_marks(num)

print("Sum =", result)
print("Choose a Operation")
print("1. Sqaure")
print("2. Cube")

def square(x):
    return x * x

def cube(x):
    return x ** 3

def apply_operation(func, value):
    return func(value)

o = input("Enter Operation (square/cube): ").strip().lower()
num = int(input("Enter Number: "))

if o == "square":
    c = square
elif o == "cube":
    c = cube
else:
    c= None
    print("Invalid operation selected.")


if c:
    result = apply_operation(c, num)
    print(f"The result of {o} on {num} is: {result}")

import random as r
x = r.randint(1,10)
i=0
while i<5:
    try:
        j=int(input("Guess the number (1-10): "))
        i+=1
        if x==j:
            print(f"u guessed the number {j} is the number")
        else:
            print(f"guess again {j} is not the number")
    except ValueError:
        print("Not a valid Number")
else:
    print(f"\nGame over! You've run out of attempts. The correct number was {x}.")
    

#Date : 22.06.2026
class Dog:
    species = "Canine"

    def bark(self):
        print("Woof!")
dog1 = Dog()
dog2 = Dog()
dog1.bark()

class Book:
    
    def __init__(self,title,author,is_borrowed=False):
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed
        
    def display_info(self):
        print(f"Title : {self.title},author : {self.author}, Borrowed : {self.is_borrowed}")

book1 = Book("Tomb of Sand","Geetanjali Shree")
book2 = Book("Adam","S. Hareesh",True)
book3 = Book("The Bench","Jhumpa",True)
book1.display_info()
book2.display_info()
book3.display_info()

class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance

    def deposit(self,amount):
        if 0<=amount<=self.balance:
            self.balance+=amount
            print(f"Your deposited amount{amount},your current balance {self.balance}")
            
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"Your withdraw amount{amount},your current balance {self.balance}")
            
        elif self.balance<amount:
            print("Insuffecient Balance")
            
s = BankAccount(int(input("Enter your current balance")))
d = input("Select opperation (Deposit(d)/Withdraw(w))")

if d.lower() == "d":
    s.deposit(int(input("Enter Amount")))
elif d.lower() == "w":
    s.withdraw(int(input("Enter Amount")))

class Rectangle:
    def __init__(self,length=2,breadth=3):
        self.length=length
        self.breadth=breadth

    def area(self):
        print(f"Area when lenght is {self.length} breadth is {self.breadth} and area is" , self.length*self.breadth)

    def perimeter(self):
        print(f"Area when lenght is {self.length} breadth is {self.breadth} and perimeter is", 2*(self.length+self.breadth))

l = int(input("Enter length"))
b = int(input("Enter breadth"))
r = Rectangle()
d = input("Select opperation (Area(a)/Perimeter(p))")
if d.lower() == "a":

    r.area()
else:
    r.perimeter()

#Date : 22.06.2026

class Ticket:
    def __init__(self,movie,seats_available,seats_requested):
        self.movie=movie
        self.seats_available=seats_available
        self.seats_requested=seats_requested
    def confirmed(self):
        if self.seats_requested<=self.seats_available:
            print(f"Your ticket for {self.movie} is confirmed")
        else:
            print(f"Sorry, your ticket for {self.movie} is not confirme)
Ticket(input("Enter movie name: "),int(input("Enter available seats: ")),int(input("Enter requested seats: "))).confirmed()

class Employee:
    def __init__(self,name,department="General",bonus=0):
        self.name=name
        self.department=department
        self.bonus=bonus
    def annual_summary(self,salary=30000):
        salary+=self.bonus
        print(f"{self.name} of {self.department} department has salary {salary} including bonus of {self.bonus}.")
Employee("Yash","Technical",3000).annual_summary(1000000)
Employee("Rohan","Designing",10).annual_summary()
Employee("Alex").annual_summary()

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def total_value(self):
        return self.price * self.quantity

    def display_product_details(self):
        l = [self.name, self.price, self.quantity]
        print(f"Product Data List: {l}")
        print(f"Calculated Total Value inside method: {self.total_value()}")

Product("Laptop", 50000, 2).display_product_details()  
Product("Smartphone", 20000, 3).display_product_details()
p=Product("Tablet", 15000, 4)
p.display_product_details()
print(f"Direct call to total_value(): {p.total_value()}")
#date : 24.06.2026

class Employee:
    company = "KRM Corp"       # class variable
    _count = 0                 # protected class variable
    
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
        Employee._count += 1
        
    @classmethod               # receives class, not instance
    def get_count(cls):
        return f"{cls.company} has {cls._count} employees"
        
    @staticmethod              # no cls or self - pure utility
    def validate_dept(dept):
        valid = ["CSE", "ECE", "MBA", "MCA"]
        return dept in valid

e1 = Employee("Alice", "CSE")
e2 = Employee("Bob",   "ECE")

print(Employee.get_count()) 
# KRM Corp has 2 employees

print(Employee.validate_dept("CSE")) # True

class Student:
    total_students = 0
    def __init__(self, roll_no, marks_list):
        self.__roll_no = roll_no
        self.__marks = []
        self._grade = "Pending"      
        self.gpa = marks_list
        Student.total_students += 1

    @property
    def gpa(self):
        avg = sum(self.__marks) / len(self.__marks)
        return avg / 10
    
    @gpa.setter
    def gpa(self, marks_list):
        for m in marks_list:
            if m < 0 or m > 100:
                print("Error: Marks should be between 0 and 100")
                return
        self.__marks = marks_list
        
       
        c_gpa = self.gpa
        if c_gpa >= 9:
            self._grade = "A"
        elif c_gpa >= 7.5:
            self._grade = "B"
        elif c_gpa >= 5:
            self._grade = "C"
        else:
            self._grade = "D"

    @classmethod
    def count(cls):
        return cls.total_students


s1 = Student("21", [80, 90, 85])
print("GPA:", s1.gpa)
print("Grade:", s1._grade)
print("Total Students:", Student.count())
s2 = Student("22", [70, 75, 80])
print("GPA:", s2.gpa)       
print("Grade:", s2._grade)
print("Total Students:", Student.count())
'''
#inheritance
class A:
    def __init__(self):
        print("class A is called")
class B(A):
    def __init__(self):
        print("Class B is called")
        super().__init__()
class C(B):
    def __init__(self):
        print("Class C is called")
        super().__init__()
        
c = C()










        

