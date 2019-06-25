#This program will demo if/else structure and the main() function



##def main():
##    print("Steve")
##    x=input("Enter a value: ")
##    print(x)
##
##def johnboyandbilly():
##    print("John")
##    print("Billy")
##main()
##johnboyandbilly()


def main():
    gradeScale()
##    
##def gradeScale():
##    grade=int(input("Enter a numeric grade: "))
##    if grade >= 90:
##        print("You made an A")
##    else:
##        if grade > 79:
##            print("You made a B")
##        else:
##            if grade > 69:
##                 print("You made a C")
##            else:
##                if grade > 59:
##                    print("You made a D")
##                else:
##                    print("You made an F")
##
##
##
##main()


def gradeScale():
    grade=int(input("Enter a numeric grade: "))
    if grade >= 90:
        print("You made an A")
    elif grade > 79:
        print("You made a B")
    elif grade > 69:
        print("You made a C")
    elif grade > 59:
        print("You made a D")
    else:
        print("You made an F")



main()
