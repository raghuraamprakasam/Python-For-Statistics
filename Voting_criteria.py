citizen = input("Which citizen you are:")
if citizen == "Indian" or citizen == "indian":
    age = int(input("Enter the age:"))
    if age >=18:
        vote = input("Have voter id (Yes/No):")
        if vote == "Yes" or vote == "yes":
            print("You are eligible to vote for the upcoming election") 
        else:
            print("Sorry you dont have voter id")
    
    else:
        print("You are not eligible since you are below 18")

else:
    print("You are not eligible to vote")
