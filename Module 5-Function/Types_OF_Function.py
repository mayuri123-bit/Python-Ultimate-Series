#............It is reusable block of code that can used to perform specific task
#Example 1
def greet():
    print("Hello,Welcome")

greet()

#parameters---values passed to function by calling the function
def para(name):
    print("Hello", name)

para("Mayuri")
para("Ishika")

#Multiple Parameters
def fun(a,b):
    print(a+b)

fun(10,20)
fun(100,20)

#Keyword arguments
def key(name,age):
    print("Name-",name)
    print("Age-",age)

key(name="Mayuree",age=20)

#arg-Allows Function to accept multiplepostional arguments
def function(*Numbers):
    print("total",sum(Numbers))

function(10,20,30,40)
function(1000,2000)
###Another example
def display(*names):
    for name in names:
        print(name)

display("mayuri","ishika","Ishaa")

#(**Kwargs)---Allows mutiple keyword aaaarguments
def stdinfo(**details):
    print("Student Info:",details)

stdinfo(name="Mayuri",age=20,Batch="Tybcs")

#Loop through **kwargs(key word arguments)
#+ef loop(**kwargs):
  #  for looping in **kwargs:
     #   print(**kwargs)