gender = input("Enter the gender:")
age= int(input("Enter the age:"))
if gender == "male" or gender == "Male":
    if age >=25:
        print("Allowed")
    else:
        print("Not allowed")
else:
    if age >=21:
        print("Allowed")
    else:
        print("Not allowed")
