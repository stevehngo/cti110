# CTI-110
# P3HW2 - MealTipTax
# Steve Ngo
# 6-25-2019
#

#Psudocode
# 1.)Declare Variables

# 2.)Prompt user for the cost of the meal
# 3.)Calculate the tip amount of the meal at 15%, 18%, and 20% using the formula:
#    tip = meal cost * (.15, .18, and .2)
# 4.)Display the values of the tip at 15%, 18%, and 20%
# 5.)Ask user to enter the tip percentage they would like to consider (15% or 18% or 20%)
# 6.)Create if statement to determine the calculation used based on user tip percent input
# 7.)Calculate the total cost of the meal with tip and sales tax using the formula:
#    total = cost + (tip * cost) + (cost * .07)
# 8.)Display an error if user enters another percentage
# 9.)Display all of these amounts ( tip, tax and total).

#Declare Variables
cost = 0.0
total = 0.0
tip = 0.0
fifteenTip = 0.0
eighteenTip = 0.0
twentyTip = 0.0
tax = 0.0

# Prompt user for the cost of the meal

cost = float(input("Enter the cost of the meal: "))

# calculations

fifteenTip=cost*.15
eighteenTip=cost*.18
twentyTip=cost*.2
tax=cost*.07

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

# ask user for recomended tip
def main():
    tip=int(input("Enter one of the following tip percentages recommended: "))
    print()

    # if statement w/ calculations

    if tip == 15:
        tip=cost*.15
        total=cost+(tip)+(tax)
    elif tip == 18:
        tip=cost*.18
        total=cost+(cost*.18)+(tax)
    elif tip == 20:
        tip=cost*.2
        total=cost+(cost*.2)+(tax)
    #display error message
    else:
        print("Invalid tip ammount, please use tip percentages provided.")
        main()

#display totals
    print("Your total is: ")
    print()
    print(("Tax").ljust(10) + str(format(tax,'.2f')).rjust(10))
    print(("Tip").ljust(10) + str(format(tip,'.2f')).rjust(10))
    print(("Total").ljust(10) + str(format(total,'.2f')).rjust(10))
    print()
    print("Have a nice day!")
main()

