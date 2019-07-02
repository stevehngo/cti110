# This program will use a loop to keep a running total of bugs collected
#   during seven days
# 7-2-2019
# CTI-110 P4T2 - Bug Collector
# Steve Ngo
#


#Psudocode
# 1.) Initialize accumulator
# 2.) Create a 'for' loop using 'day' as a variable and a range of 1 through 7
# 3.) Prompt user for input of bugs collected on a single day
# 4.) Input number of bugs
# 5.) Use formula to calc total bugs
#   total+=bugs
# 6.) Display total bugs collected


# Initialize accumulator
total = 0

# Get bugs collected for each day
for day in range(1, 8):
    # prompt user
    print('Enter the bugs collected on day', day)
    
    # Input number of bugs
    bugs = int(input())

    # Add bugs to total
    total = total + bugs # or total += bugs

# Display the total bugs
print ('You collected a total of', total, 'bugs')
