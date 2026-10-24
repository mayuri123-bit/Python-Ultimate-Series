#File handling
file=open("Sample.txt","r")

content=file.read()

print(content)

#Read One line
file=open("Sample.txt","r")
print(file.readline())
print(file.readline())

#Read all  lines
file=open("Sample.txt","r")
allines=file.readlines()
print(allines)
#['Hello Mayuri\n', 'Welcome to Python\n', 'File Handling is easy.']

file.close()