# This program uses a loop to display a table of pounds starting from 100 through 300
#   (with a step value of 10) and their equivalent kilograms using the formula
#   kg= lb/2.2046 .
# 6-27-2019
#CTI-110 P4HW2 - Pounds to Kilos Table
#Steve Ngo
#

#psudocode
# 1.)Display Variables
# 2.)Print Header
# 3.)Print weight from lb to kg using formula:
#       kg=lb/2.2046

# display variables
start = 100
end = 300
increment = 10
math = 2.2046

# print header
print("This program displays a weight in pounds")
print("and converts it to kilograms.")
print()
print("Pounds\tKilograms")
print("-----------------")

# print weight from lb to kg
for pounds in range (start, end+1, increment):
    kilograms = pounds / math
    print(pounds, '\t', format(kilograms, '.2f'))
