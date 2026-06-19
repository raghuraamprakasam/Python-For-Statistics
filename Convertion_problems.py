# COnvert Hours to minutes and seconds
"""hours = float(input("Enter the number of hours: "))
minutes = hours * 60
seconds = hours * 36
print("The hours:",hours)
print("The minutes",minutes)
print("The seconds",seconds)"""

# convert years to months and days
"""years = int(input("Enter the number of years: "))
months = years * 12
days = years * 365
print("The years:",years)
print("The months",months)
print("The days",days)"""

#combining both
"""years = int(input("Enter the number of years: "))
months = years * 12
days = years * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print("The years:",years)
print("The months",months)
print("The days",days)
print("The hours:",hours)
print("The minutes",minutes)
print("The seconds",seconds)"""

# coversion of miles per hour to km per hour
mile = float(input("Enter speed of the vehicle:"))
km_h = mile*1.6094
km_m = km_h / 60
km_s = km_h /3600
meter = km_h * 1000
centi_meter = meter*100
print("The converted speed of mile to km per hour:",km_h)
print("The converted speed of mile to meter per hour:",meter)
print("The converted speed of mile to centi meter per hour:",centi_meter)
print("The converted speed of mile to km per minute:",km_m)
print("The converted speed of mile to km per seconds:",km_s)


