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
    """
    Madlibs theme number 1
    """
    print(
        colored("Instructions for the Babysiter")
    )
    adjective11 = input(colored("adjective:\n", "blue", attrs=["bold"]))
    plural_nou11 = input(colored("plural noun:\n", "blue", attrs=["bold"]))
    plural_nou12 = input(colored("A plural noun:\n", "blue", attrs=["bold"]))
    plural_nou13 = input(colored("more plural noun:\n", "blue", attrs=["bold"]))
    plural_nou14 = input(colored("A plural noun:\n", "blue", attrs=["bold"]))
    adverb11 = input(colored("An adverb:\n", "blue", attrs=["bold"]))
    noun11 = input(colored("One noun:\n", "blue", attrs=["bold"]))
    noun12 = input(colored("Another noun:\n", "blue", attrs=["bold"]))

    if adjective11.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs01()
    elif plural_nou11.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs01()
    elif plural_nou12.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs01()
    elif plural_nou13.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs01()
    elif plural_nou14.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs01()
    elif adverb11.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs01()
    elif noun11.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs01()
    elif noun12.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs01()
    else:
        madlibs1 = print(colored(
            f"The boys can watch an hour of {adjective11} television " +
            f"before turning off the {plural_nou11} in their room." +
            f"Make sure they do not watch any violent {plural_nou12}" +
            f"or adult {plural_nou13}" +
            f". If there are any phone {plural_nou14}," +
            f"do not identify yourself as the {adverb11}-sitter." +
            f"Take a message. Write it {noun11} " +
            f"on the {noun12} provided.",
            "yellow", attrs=["bold"])
        )


def madlibs02():
    """
    Madlibs theme number 2
    """
    print(
        colored("Going to the doctor")
    )
    adjective21 = input(colored("An adjective:\n", "blue", attrs=["bold"]))
    adjective22 = input(colored("An adjective:\n", "blue", attrs=["bold"]))
    adjective23 = input(colored("Another adjective:\n", "blue", attrs=["bold"]))
    adjective24 = input(colored("Adjective please:\n", "blue", attrs=["bold"]))
    adjective25 = input(colored("Adjective again:\n", "blue", attrs=["bold"]))
    place11 = input(colored("A place:\n", "blue", attrs=["bold"]))
    pieceofcloth21 = input(colored("Some clothing:\n", "blue", attrs=["bold"]))
    bodypart21 = input(colored("a body part:\n", "blue", attrs=["bold"]))
    bodypart22 = input(colored("another body part:\n", "blue", attrs=["bold"]))
    bodypart23 = input(colored("a third body part:\n", "blue", attrs=["bold"]))
    noun21 = input(colored("a noun:\n", "blue", attrs=["bold"]))
    noun22 = input(colored("a second noun:\n", "blue", attrs=["bold"]))
    place22 = input(colored("another place:\n", "blue", attrs=["bold"]))

    if adjective21.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif adjective22.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif adjective23.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif adjective24.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif adjective25.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif place11.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif pieceofcloth21.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif bodypart21.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif bodypart22.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif bodypart23.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif noun21.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif noun22.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif place22.isalpha() is False:
        pprint(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    else:
        madlibs2 = print(colored(
            f"Every year, you visit the doctor. It is very {adjective21}. " +
            f"Usually you have to skip going to {place21} to go." +
            f"Your doctor is usualy a {adjective22} person" +
            f"who is wearing a/an {adjective23} {pieceofcloth21}." +
            " They will look at your {bodypart21}" +
            f", {bodypart22} and {bodypart23}." +
            f"They can be very {adjective24}. Afterwards," +
            f"they will give you a {noun21} and a " +
            f"{noun22}, and then you will go to {place22} as a treat." +
            f" All in all, the doctor's office isn't so {adjective25}.",
            "yellow", attrs=["bold"])
        )


def madlibs03():

    """
    Madlibs theme number 3
    """
    print(
        colored("Bats are so cool.")
    )
    color31 = input(colored("A color:\n", "blue", attrs=["bold"]))
    adjective31 = input(colored("An adjective:\n", "blue", attrs=["bold"]))
    time31 = input(colored("A time of day:\n", "blue", attrs=["bold"]))
    adjective32 = input(colored("Second adjective:\n", "blue", attrs=["bold"]))
    place31 = input(colored("A place:\n", "blue", attrs=["bold"]))
    food31 = input(colored("Food:\n", "blue", attrs=["bold"]))
    food32 = input(colored("Some more food:\n", "blue", attrs=["bold"]))
    verb31 = input(colored("A verb:\n", "blue", attrs=["bold"]))
    noun31 = input(colored("A noun:\n", "blue", attrs=["bold"]))

    if color31.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs03()
    elif adjective31.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs03()
    elif time31.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs03()
    elif adjective32.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs03()
    elif place31.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs03()
    elif food31.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs03()
    elif food32.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs03()
    elif verb31.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs03()
    elif noun31.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs03()
    else:
        madlibs3 = print(colored(
            f"Bats are {color31}, {adjective31} animals which have wings. " +
            f"They fly around at {time31} which scares people. " +
            f"Bats are {adjective32}. My pet bat lives in {place31}. " +
            f"I like to feed him {food31} and" +
            f"{food32}. He likes to {verb31}. " +
            f"I am his favorite person, but he also likes {noun31}. ",
            "yellow", attrs=["bold"])
        )


def main_choice():
    selection = int(input(colored(
        "select your theme:\n", "blue", attrs=["reverse", "blink"]
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
