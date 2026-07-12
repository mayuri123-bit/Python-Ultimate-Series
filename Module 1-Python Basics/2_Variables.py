#.....................Variables in Python.......................
#--->Used to store Values by using variables (variable=container that stores values)

#program 1- Store and print a variable
name="mayuri"
city="Nanded"
age=20
print("My name is ",name)
print("I am from ",city)
print("I am ",age,"years old")

#Program-2 Multiple Assignment
a,b,c=10,20,30
print("Value of a is ",a)
print("Value of b is ",b)
print("Value of c is ",c)

#Program-3 Assigning same value to multiple variables
x=y=z=100
print("Value of x is ",x)
print("Value of y is ",y)

#Program-4 Swapping of two variables
a=10
b=20
print("Before swapping a is ",a)
print("Before swapping b is ",b)
temp=a
a=b
b=temp
print("After swapping a is ",a)
print("After swapping b is ",b)

#Program-5 Swamming Variables without using Third variable
x,y=100,200
print("Before swapping x=",x,"\nBefore swapping y=",y)
x,y=y,x
print("After swapping x=",x,"\nAfter swapping y=",y)

