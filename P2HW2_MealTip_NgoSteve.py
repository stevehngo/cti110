# This program will calculate the total amount of a meal purchased at a restaurant
# 6-18-2019
# CTI-110 P2HW2 - Meal Tip Calculator
# Steve Ngo
#

#Psudocode
# 1.)Declare Variables
#    Meal Cost = 0 float
#    Tip = 0 float
#    Total = 0 float
#    FifteenTip = 0 float
#    EighteenTip = 0 float
#    TwentyTip = 0 float
#    fTotal = 0.0
#    eTotal = 0.0
#    tTotal = 0.0
# 2.)Prompt user for the cost of the meal
# 3.)Calculate the tip amount of the meal at 15%, 18%, and 20% using the formula:
#    tip = meal cost * (.15, .18, and .2)
# 4.)Display the values of the tip at 15%, 18%, and 20%
# 5.)calculate the total cost of the meal using the formula:
#    total = meal cost + tip ammount
# 6.)Display the total cost of the meal at each percentage

# declare variables

mealCost = 0.0
total = 0.0
tip = 0.0
cusTip = 0.0
fifteenTip = 0.0
eighteenTip = 0.0
twentyTip = 0.0
fTotal = 0.0
eTotal = 0.0
tTotal = 0.0

# Prompt user for the cost of the meal

mealCost = float(input("Enter the cost of the meal: "))

# calculations

fifteenTip=mealCost*.15
eighteenTip=mealCost*.18
twentyTip=mealCost*.2

# display the values of the tip at 15%, 18%, and 20%
title = "Recomended Tip"
fifteenHdg = "15%"
eighteenHdg = "18%"
twentyHdg = "20%"

print()
print(title.center(30))
print()
print(fifteenHdg.ljust(10) + eighteenHdg.center(10) + twentyHdg.rjust(10))
print()
print(str(format(fifteenTip,'.2f')).ljust(10) + str(format(eighteenTip,'.2f')).center(10) + str(format(twentyTip,'.2f')).rjust(10))
print()

# calculate

fTotal=mealCost+fifteenTip
eTotal=mealCost+eighteenTip
tTotal=mealCost+twentyTip

# Display the total cost of the meal at each percentage

print("Total".center(30))
print()
print(str(format(fTotal,'.2f')).ljust(10) + str(format(eTotal,'.2f')).center(10) + str(format(tTotal,'.2f')).rjust(10))
