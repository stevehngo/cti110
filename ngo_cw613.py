#Steve Ngo
#6-13-2019
#ngo_613
#This program will calculate the amount paid for a car payment per month

##num=0 #integer variable
##value=0.0 #float variable
##
##name="Steve" #string variable
###variable reassignment
##num="0"
##
##print(num)
##
##print(value)
##
##print(name)



payment=float(input("Enter the car payment amount: "))

month=int(input("Enter the # of months paid: "))

total = payment * month

print("The total amount paid is ", total, ".")

print("The total amount paid is " + str(total) + ".")
