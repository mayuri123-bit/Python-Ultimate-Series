#....Nested If----It is and if condition that contain one more if condition within it
username=input("Enter your Username:")
password=input("Enter Password:")
if username=="admin":
    if password=="1234":
        print("Login Sucuessful")
    else:
        print("Wrong Password")
else:
    print("Something Wents wrong Invalid Username")
