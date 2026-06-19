
# calculate greates common divider of A and B 
a=int(input("Enter the value fo a:"))
b=int(input("Enter the value of b:"))
while (a!=b):
    if a>b:
        a=a-b
    else:
        b=b-a
print(a,"Is the GCD")
