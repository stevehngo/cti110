# This program uses a loop to display the amount of calories burned on a tredmill
#   after running 25, 35, and 45 minutes at 5 callories burned per minute.
# 6-27-2019
#CTI-110 P4HW1 - Calories Burned
#Steve Ngo
#

#Psudocode
# 1.)Display program function
# 2.)Declare Variables
# 3.)Print table header
# 4.)Print the minutes ran and the calories burned

# display program function
print("This program  displays the amount of calories burned on a tredmill")
print("at 25, 35, and 45 minutes.")

# declare variables
increment = 10
end = 45

# print table headings
print()
print("Minutes\tCalories")
print("-----------------")

# print the minutes ran and the calories burned
for number in range (25, end+1, increment):
    cal = number*5
    print(number, '\t', cal)
