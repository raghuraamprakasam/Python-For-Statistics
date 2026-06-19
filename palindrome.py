# check if a number is palidrome or not
num = input("Enter the number:") 
if num == num[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
