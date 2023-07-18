import sys

from termcolor import colored, cprint


def opening_function():

    """
    This is the welcome message and the instructions
    """
    print(colored(
        "Welcome to Random Madlibs.\n" +
        "Please select the theme of your madlibs:\n" +
        "Type 1 for Instructions for the Babysiter.\n"
        "Type 2 for Going to the doctor.\n"
        "Type 3 for Bats are so cool.\n",
        "yellow", attrs=["bold"]))
    main_choice()


def madlibs01():
    print("MADLIBS 1 HERE")

def madlibs01():
    print("MADLIBS 2 HERE")

def madlibs01():
    print("MADLIBS 3 HERE")


def main_choice():
    selection = int(input(colored(
        "select Madlibs theme: ", "blue", attrs=["reverse", "blink"]
        )))

    """
    This function allows the user to select a theme
    """
    if selection == 1:
        madlibs01()
    elif selection == 2:
        madlibs02()
    elif selection == 3:
        madlibs03()
    else:
        print("Invalid selection, please try again")
        main_choice()


def main():
    opening_function()


main()
