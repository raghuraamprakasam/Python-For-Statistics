# simple login verification
user = input("Username: ")
pwd = input("Password: ")

if user == "admin" and pwd == "1234":
    print("Login Successful")
else:
    print("Invalid username or password")
