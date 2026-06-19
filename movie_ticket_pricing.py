# movie ticket pricing based on age
christ = input("Are you an christ university student:")
age = int(input("Enter the age:"))
rate = 500
if christ == "Yes" or "yes":
    print("You are eligible for discounts")
    if age<8:
        rates = rate - (rate)*(20/100)
        print("The price of your ticket will be:",rates)
    elif age<25:
        rates = rate - (rate)*(10/100)
        print("The price of your ticket will be:",rates)
    else:
        rates = rate - (rate)*(5/100)
        print("The price of your ticket will be:",rates)
else:
    print("No discounts are available for you.")
    print("The rate of your ticket will be:",rate)
    
        
