#!/usr/bin/pythonw
# Program for doing math

# Define the clear function, which clears the screen.


def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# Define the print_menu function, which displays the menu.


def print_menu():
    print ("           +------------------------------------------+ ")
    print ("           |    Menu to show any of the following:    | ")
    print ("           + -----------------------------------------+ ")
    print ("")
    print ("  1. Fibonacci Sequence                  5. Option 5")
    print ("  2. Option 2                            6. Option 6 ")
    print ("  3. Option 3                            7. Help")
    print ("  4. Option 4                            8. Quit")
    print ("")


# define the help fuction

def help_function():
    clear()             # Clear the screen
    print ("This is the help function")
    print ("")
    print ("This program was written in Python by Jeremy Tang.The purpose of")
    print ("this program is to perform mathematcical expressions from a menu")
    print ("driven interface.")
    print ("This program was written to complement a CS class at Stuyvesant")
    print ("")
    input("Hit the <Enter> key to continue...")


# Fibonacci Sequence Function
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))


# main

clear()             # Clear the screen when we start

loop = True

while loop:         # While loop which will keep going until loop = False
    print_menu()    # Displays menu
    choice = input("Enter your choice [ 1 - 8 ]: ")

    if choice == "1":
        nterms = int(input("How many terms? "))
        if nterms <= 0:
            print("Plese enter a positive integer")
        else:
            print("Fibonacci sequence:")
            for i in range(nterms):
                print(recur_fibo(i))

    if choice == "2":
        print ("option 2")
        clear()
        print_menu

    elif choice == "3":
        print ("option 3")
        clear()
        print_menu

    elif choice == "4":
        print ("option 4")
        clear()
        print_menu

    elif choice == "5":
        print ("option 5")
        clear()
        print_menu

    elif choice == "6":
        print ("option 6")
        clear()
        print_menu

    elif choice == "7":
        help_function()

    elif choice == "8":
        print ("bye!")
        # You can add your code or functions here
        # This will make the while loop end.
        loop = False
