"""count = 0
while (count<10):
    count = count +1
    print(count,"My name is raghuraam")"""

#calculator using while loop
"""print("Enter 1 for addition.\n"
      "Enter 2 for subraction.\n"
      "Enter 3 for multiplication.\n"
      "Enter 4 for division.\n"
      "Enter 5 for power,\n"
      "Enter 0 to exit.")    
x=int(input("Enter a number to do arithmetic operation:"))
while (x!=0):
    match x:
        case 1:
            a = int(input("Enter the value of A"))
            b = int(input("Enter the value of B"))
            print("The addition operation = ",a+b)
            x=int(input("Enter the next operation to do:"))
        case 2:
            a = int(input("Enter the value of A"))
            b = int(input("Enter the value of B"))
            print("The subraction operation = ",a-b)
            x=int(input("Enter the next operation to do:"))
        case 3:
            a = int(input("Enter the value of A"))
            b = int(input("Enter the value of B"))
            print("The Multiplication operation = ",a*b)
            x=int(input("Enter the next operation to do:"))
        case 4:
            a = int(input("Enter the value of A"))
            b = int(input("Enter the value of B"))
            print("The Division operation = ",a/b)
            x=int(input("Enter the next operation to do:"))
        case 5 :
            a = int(input("Enter the value of A"))
            b = int(input("Enter the value of B"))
            print("The power operation = ",a**b)
            x=int(input("Enter the next operation to do:"))
        case _:
            print("Enter a valid number between 0 and 5")
            x=int(input("Enter the next operation to do:"))
print("The process have been exited")"""

# Validating the scret number
"""x = int(input("Enter the secret number, it is a one digit number:"))
secret_number = 9
while (x!=secret_number):
    print("The secret number is incorrect")
    x = int(input("Another number"))
print("The secret number is correct")"""


user = int(input("enter"))
count = user
while True:
    print(count)
    count = count -1
    if count == -1:
        break
        
        
        
            
            
            
    


            
    
