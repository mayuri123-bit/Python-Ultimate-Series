with open("Sample.txt","r") as file:
    print(file.read())

with open("Sample.txt","w") as file:
    content=file.write("Mayuri Narwade")
    print(content)