# printing star in triangle format

"""n = int(input("Enter  a value:"))
for i in range(n):
    for j in range(i):
        print("*",end="")
    print("\n")
print("end")"""


# another pattern of star
"""n = int(input("Enter  a value:"))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print("\n")
print("end")"""


# another pattern of star
"""n = int(input("Enter  a value:"))
for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print("\n")
print("end")"""


# another pattern of star
"""n = int(input("Enter  a value:"))
for i in range(n):
    for k in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print("\n")
print("end")"""


# another pattern of star
"""n = int(input("Enter  a value:"))
for i in range(1,n+1):
    spaces = " "*(n-i)
    stars = "*"*(2*i-1)
    print(spaces+stars)
print("end")"""


# another pattern of star
"""
n = int(input("Enter  a value:"))
for i in range(1,n):
    spaces = " "*(n-i)
    stars = "*"*(2*i-1)
    print(spaces+stars)
for i in range(n,0,-1):
    spaces = " "*(n-i)
    stars = "*"*(2*i-1)
    print(spaces+stars)
print("end")"""


# using numbers same
"""n = int(input("Enter  a value:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")
print("end")"""


n = int(input("Enter  a value:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j*i,end=" ")
        j= j+1
    print("\n")
print("end")




