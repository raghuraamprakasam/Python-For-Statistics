k = int(input("Enter signal value:"))
sums = 0
for x in range(k):
    x = 1/(k+1)
    sums = sums + x
print("The total signals received is:",sums)
