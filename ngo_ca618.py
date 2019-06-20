# Steve Ngo
# ngo_cw618
# 6-18-2019
# This program will calculate the area of a triangle

#Psudocode
# 1.)Declare Variables
#    Base = 0 float
#    Height = 0 float
#    area = 0 float
#    HALF = .5 float
# 2.)Prompt user for the base and height of the triangle
# 3.)Calculate the area of the triangle using the following formula:
#    area = .5base * height
# 4.)Display the area of the triangle


# declare variables

base = 0.0
height = 0.0
area = 0.0
HALF = .5

# prompt user for the height and base

base = float(input("Enter the base of the triangle: "))

height = float(input("Enter the height of the triangle: "))

# calculations

area=HALF*base*height
#or area=.5*base*height

# display area of the triangle

##print("The area of the triangle is " + str(area))
##
##print("the area of the triangle is ", format(area,'.2f' ),".",sep='', end='')
##
##print("The area of the triangle is " + str(area))

#extra

title = "Triangle"
baseHdg = "Base"
heightHdg = "Height"
areaHdg = "Area"
print(title.center(30))
print()
print(baseHdg.ljust(10) + heightHdg.ljust(10) + areaHdg.ljust(10))
print()
print(str(format(base,'.2f')).ljust(10) + str(height).ljust(10) + str(area).ljust(10))
