# CTI-110
# P3HW1 - Color Mixer
# Steve Ngo
# 6-20-2019
#

#psudocode
# 1.)Prompt user for primary color inputs
# 2.)Display results of mixing two colors using the following:
#    red + blue = purple
#    red + yellow = orange
#    blue + yellow = green
# 3.)Include error message if user inputs foregn variables

# extra
print("Primary Color Mixer".center(30))
print("Please input two primary colors.")
print("Primary colors are: red, blue, and yellow")
print()

# prompt user for primary colors
prime1 = str(input("Enter a primary color: "))
prime2 = str(input("Enter a primary color: "))
print()
 # display results
if (prime1 == "red" and prime2 == "blue") or (prime1 == "blue" and prime2 == "red"):
    print(prime1 + " mixed with " + prime2 + " is purple. ")
    
elif (prime1 == "red" and prime2 == "yellow") or (prime1 == "yellow" and prime2 == "red"):
    print(prime1 + " mixed with " + prime2 + " is orange. ")

elif (prime1 == "blue" and prime2 == "yellow") or (prime1 == "yellow" and prime2 == "blue"):
    print(prime1 + " mixed with " + prime2 + " is green. ")

# error message
else:
    print("Error please use primary colors.")
