#................Datatypes in Python................
#-->datatypes used to store different types of data 

#Program 1- Different datatypes in python
a = 10 #int
b = 10.5 #float
c = "Python" #string
d = True #boolean
e = [1, 2, 3] #list 
f = (1, 2, 3) #tuple
g = {1, 2, 3} #set
h = {"name": "Mayuri"} #dictionary
i='A' #char

#type(variable)-----> return type of variable
print("Type of a is ", type(a))
print("Type of b is ", type(b))
print("Type of c is ", type(c))
print("Type of d is ", type(d))
print("Type of e is ", type(e))
print("Type of f is ", type(f))
print("Type of g is ", type(g))
print("Type of h is ", type(h))
print("Type of i is ", type(i))

#Program 2- Typeconversion in python
num=100
print(float(num))
print(str(num))

#Program 3- Input & Output
new=input("Enter your name: ")
print("Hello",new)

#program 4 - Sum of two numbers
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("Sum of two numbers is: ",num1+num2)

#program 5- Area of triangle
base=100
height=20
area=0.5*base*height
print("Area of triangle is: ",area)

#program 6- Calculate Simple intersest
p=int(input("Enter principle amount: "))
r=int(input("Enter rate of interest: "))
t=int(input("Enter time in years: "))
si=(p*r*t)/100
print("Simple interest is: ",si)

