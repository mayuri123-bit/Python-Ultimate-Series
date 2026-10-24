file=open("Sample.txt","a")
file.write("\n This is an Sample file for File handling.")
print("Data Appended Successfully")

Content=open("Sample.txt","r")
print(Content.read())
file.close()
Content.close()