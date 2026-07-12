#..........TYPES operator.............
#---> Operators are used to perform operation (Operator =symbols that perform operation on data)

# Arithmatic operator --> Used for mathmatical operation
a = 10
b = 2
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Floor Division =", a // b)
print("Modulus =", a % b)
print("Power =", a ** b) 

#Assigned operator ---->Used for store and update values in variable
a=100
c=a
print("value of a:",c)
a+=5
print("a=a+5",a)
a-=5 
print("a=a+5",a )
a*=10
print("a=a*10",a)
a /=2
print("a=a/2",a)

#Comparison Operator---> used to compare values
a=100
b=200
print(a==b)#Equal?
print(a!=b)#nor Equal?
print(a>b) 
print(a<b)
print(a<=b)
print(a>=b)

#Logical Operator---> Used For logical operation
age=20
citizen=True
print(age>=18 and citizen)# True AND True= True remaining all False
print(age>=18 or citizen) # False OR False Remaining all True
print( not citizen )# print opposite Values

#identity operator --->used to check that the variables are exact same having same memory location or not
a=[10,20,30]
b=a # same values + Same memory location
c=[10,20,30] # same values + different memory location
print( b is a) #exact same= True
print(a==b) 
print(c is b) #False --> Memory location is different
print(a is not c) #True

#Membership operator --> determines values are member or not of given variable
fruit=["apple","Mango","bannana"]
print("apple" in fruit)
print("orange " in fruit)
print("orange " not in fruit)

#Bitwise operator --->operators that perform operations directly on the binary bits ( 0 , 1) of integer values
a=5
b=3
print("AND=",a & b)
print("OR=",a | b)
print("XOR=",a ^ b)
print("NOT=",-a)
print("Left Shift=",a<<1)
print("Right Shift=",a>>1)

#>>>>>>>>>>>>>>>>>>>Practice Question Based on Above Concept

#program 1-------Calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)

#program 2----Compare two number
a=int(input("Enter First numbers:"))
b=int(input("Enter Second numbers:"))
if a>b:
    print("First number is greater ")
elif a==b:
    print("Equal Numbers")
else :
    print("Secong Number is highest")

#Program 3---Voting eligibility
age = int(input("Enter age: "))
print(age >= 18 and age <= 100)

#program 4---check Character
name = input("Enter your name: ")
print("a" in name)

#Program 5---Binary example
a = 12
b = 10
print(bin(a))
print(bin(b))
print(bin(a & b))
print(bin(a | b))
print(bin(a ^ b))

#Program 6---Find Square of number
num = int(input("Enter number: "))
print("Square =", num ** 2)

#Program 7 ---Celsius to Fahrenheit
c = float(input("Enter Celsius: "))
f = (c * 9 / 5) + 32
print("Fahrenheit =", f)

#Program 8----Even or odd
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#program 9---rectangle Area
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area =", area)

#program 10---Average of three numbers
a = int(input("First: "))
b = int(input("Second: "))
c = int(input("Third: "))
avg = (a + b + c) / 3
print("Average =", avg)