# swap numbers
a = 10
b = 20
b= b-a
a = a+a
print(a)
print(b)

#swap numbers by taking input from users
a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
a = a+b
b= a-b
a = a-b
print("after swapping:")
print("a=",a)
print("b=",b)
