#This program will calculate the amount paid for a car payment per month
#6-13-2019
#CTI-110 P2HW1 - Pounds to Killograms Converter
#Steve Ngo
#

#prompt the user for weights in pounds
#set pounds to a variable called pounds
#callculate value of killograms by multiplying pounds * 2.2046 and assign to a variable called kilograms
#display pounds to killograms variable tottal w/ print statement

pounds=float(input("Enter Weight in Pounds: "))

kilograms = pounds * 2.2046

print(pounds, "lbs is equivalent to", kilograms, "kg")
