# sum of digits
n = int(input("Enter a number:"))
sums = 0
while n>0:
    dig = n%10
    sums += dig
    n = n//10
print("the sum of digits:",sums)
