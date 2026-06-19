p = float(input("Enter the principal amount:"))
r = float(input("Enter the rate of interest per annum:"))
t = float(input("Enter the time period:"))
time = t/12
simple_interest = (p*r*time)/100
print("Simple interest:",simple_interest)
