#This program will calculate the greater area of two rectangles
#6-13-2019
#CTI 110 - P3T1 Area of Rectangles
#Steve Ngo
#

#psudocode
# 1.)Declare Variables
#    lenght1 = 0.0 float
#    width1 = 0.0 float
#    length2 = 0.0 float
#    width2 = 0.0 float
#    area1 = 0.0 float
#    area2 = 0.0 float
# 2.)Prompt user for the lenght and width of rectangle 1
# 3.)Prompt user for the length and width of rectangle 2
# 4.)Calculate the area of rectangle 1
# 5.)Calculate the area of rectangle 2
# 6.)Determine the following
# if area1 > area2
#       Display "Rectangle 1 has the greatest area"
#else if area2 > area 1
#       Display "Rectangle 2 has the greatest area"
#else
#       Display "Both rectangles have the same area"
#

# declare variables
lenght1 = 0.0
width1 = 0.0
length2 = 0.0
width2 = 0.0
area1 = 0.0
area2 = 0.0

# prompt user for demensions of the rectangles
length1 = float(input("Enter length of rectangle 1: "))
width1 = float(input("Enter width of rectangle 1: "))
length2 = float(input("Enter length of rectangle 2: "))
width2 = float(input("Enter width of rectangle 2: "))

# calculate

area1 = length1 * width1
area2 = length2 * width2

# determin which has the greater area

if area1 > area2 :
    print("Rectangle 1 has the greatest area.")
elif area2 > area1:
    print("Rectangle 2 has the greatest area.")
else:
    print("Both have the same area.")
