import sys

from termcolor import colored, cprint

 # This variable works with the continue_game function
afirm = "yes"


def opening_function():

    """
    This is the welcome message and the instructions
    """
    print(colored(
        "Welcome to Random Madlibs.\n" +
        "Please select the theme of your madlibs:\n",
        "yellow", attrs=["bold"]))
    print(colored(
        "Type 1 for Instructions for the babysitter.\n",
        "green", attrs=["bold"]))
    print(colored(
        "Type 2 for Going to the doctor.\n",
        "blue", attrs=["bold"]))
    print(colored(
        "Type 3 for Bats are so cool.\n",
        "magenta", attrs=["bold"]))
    main_choice()


def restart_function():

    """
    This restarts the mage and prints the themes to choos from
    and the instructions
    """
    print(colored(
        "LET'S PLAY AGAIN!.\n" +
        "Please select a new theme of your Madlibs:\n",
        "yellow", attrs=["bold"]))
    print(colored(
        "Type 1 for Instructions for the babysitter.\n",
        "green", attrs=["bold"]))
    print(colored(
        "Type 2 for Going to the doctor.\n",
        "blue", attrs=["bold"]))
    print(colored(
        "Type 3 for Bats are so cool.\n",
        "magenta", attrs=["bold"]))
    main_choice()


def continue_game():

    """
    This function asks the player if they wish to continue,
    and restarts the game if they input "yes"
    """

    continue_quest = input(colored(
        "To play again please type 'yes':\n",
        "magenta", attrs=["reverse", "blink"]
    ))

    if continue_quest == afirm:
        restart_function()
    else:  
        print(
            colored(
                "Thank you for playing!",
                "blue", attrs=["reverse", "blink"]
                )
        )
    

def madlibs01():
    """
    Madlibs theme number 1
    """
    print(
        colored("Instructions for the babysitter",
                "green", attrs=["bold"])
    )
    adjective11 = input(
        colored(
            "adjective:\n", "blue", attrs=["bold"]
            )
        )
    plural_nou11 = input(
        colored(
            "plural noun:\n", "blue", attrs=["bold"]
            )
        )
    plural_nou12 = input(
        colored(
            "plural noun:\n", "blue", attrs=["bold"]
            )
        )
    plural_nou13 = input(
        colored(
            "plural noun:\n", "blue", attrs=["bold"]
            )
        )
    plural_nou14 = input(
        colored(
            "A plural noun:\n", "blue", attrs=["bold"]
            )
        )
    adverb11 = input(
        colored(
            "An adverb:\n", "blue", attrs=["bold"]
            )
        )
    noun11 = input(
        colored(
            "One noun:\n", "blue", attrs=["bold"]
            )
        )
    noun12 = input(
        colored(
            "Another noun:\n", "blue", attrs=["bold"]
            )
        )

    if not all(x.isalpha() or x.isspace() for x in adjective11):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs01()
    elif not all(x.isalpha() or x.isspace() for x in plural_nou11):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs01()
    elif not all(x.isalpha() or x.isspace() for x in plural_nou12):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs01()
    elif not all(x.isalpha() or x.isspace() for x in plural_nou13):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs01()
    elif not all(x.isalpha() or x.isspace() for x in plural_nou14):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs01()
    elif not all(x.isalpha() or x.isspace() for x in adverb11):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs01()
    elif not all(x.isalpha() or x.isspace() for x in noun11):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs01()
    elif not all(x.isalpha() or x.isspace() for x in noun12):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
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
        continue_game()


def madlibs02():
    """
    Madlibs theme number 2
    """
    print(
        colored("Going to the doctor",
                "blue", attrs=["bold"])
    )
    adjective21 = input(
        colored(
            "An adjective:\n", "blue", attrs=["bold"]
            )
        )
    adjective22 = input(
        colored(
            "AnA second adjective:\n", "blue", attrs=["bold"]
            )
        )
    adjective23 = input(
        colored(
            "More adjective:\n", "blue", attrs=["bold"]
            )
        )
    adjective24 = input(
        colored(
            "Adjective please:\n", "blue", attrs=["bold"]
            )
        )
    adjective25 = input(
        colored(
            "Adjective again:\n", "blue", attrs=["bold"]
            )
        )
    place21 = input(
        colored(
            "A place:\n", "blue", attrs=["bold"]
            )
        )
    pieceofcloth21 = input(
        colored(
            "A piece of clothing:\n", "blue", attrs=["bold"]
            )
        )
    bodypart21 = input(
        colored(
            "a body part:\n", "blue", attrs=["bold"]
            )
        )
    bodypart22 = input(
        colored(
            "another body part:\n", "blue", attrs=["bold"]
            )
        )
    bodypart23 = input(
        colored(
            "a third body part:\n", "blue", attrs=["bold"]
            )
        )
    noun21 = input(
        colored(
            "a noun:\n", "blue", attrs=["bold"]
            )
        )
    noun22 = input(
        colored(
            "a second noun:\n", "blue", attrs=["bold"]
            )
        )
    place22 = input(
        colored(
        "another place:\n", "blue", attrs=["bold"]
        )
    )

    if not all(x.isalpha() or x.isspace() for x in adjective21):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif not all(x.isalpha() or x.isspace() for x in adjective22):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif not all(x.isalpha() or x.isspace() for x in adjective23):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif not all(x.isalpha() or x.isspace() for x in adjective24):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif not all(x.isalpha() or x.isspace() for x in adjective25):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif not all(x.isalpha() or x.isspace() for x in place21):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif not all(x.isalpha() or x.isspace() for x in pieceofcloth21):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif not all(x.isalpha() or x.isspace() for x in bodypart21):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif not all(x.isalpha() or x.isspace() for x in bodypart22):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif not all(x.isalpha() or x.isspace() for x in bodypart23):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif not all(x.isalpha() or x.isspace() for x in noun21):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif not all(x.isalpha() or x.isspace() for x in noun22):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif not all(x.isalpha() or x.isspace() for x in place22):
        pprint(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    else:
        madlibs2 = print(colored(
            f"Every year, you visit the doctor. It is very {adjective21}. " +
            f"Usually you have to skip going to {place21} to go." +
            f"Your doctor is usualy a {adjective22} person " +
            f"who is wearing a/an {adjective23} {pieceofcloth21}. " +
            f"They will look at your {bodypart21}" +
            f", {bodypart22} and {bodypart23}." +
            f"They can be very {adjective24}. Afterwards," +
            f"they will give you a {noun21} and a " +
            f"{noun22}, and then you will go to {place22} as a treat." +
            f" All in all, the doctor's office isn't so {adjective25}.",
            "yellow", attrs=["bold"])
        )
        continue_game()


def madlibs03():

    """
    Madlibs theme number 3
    """
    print(
        colored("Bats are so cool.",
                "magenta", attrs=["bold"])
    )
    color31 = input(
        colored(
            "A color:\n", "blue", attrs=["bold"]
        )
    )
    adjective31 = input(
        colored(
            "An adjective:\n", "blue", attrs=["bold"]
        )
    )
    time31 = input(
        colored(
            "A time of day:\n", "blue", attrs=["bold"]
        )
    )
    adjective32 = input(
        colored(
            "Second adjective:\n", "blue", attrs=["bold"]
        )
    )
    place31 = input(
        colored(
            "A place:\n", "blue", attrs=["bold"]
        )
    )
    food31 = input(
        colored(
            "Food:\n", "blue", attrs=["bold"]
        )
    )
    food32 = input(
        colored(
            "Some more food:\n", "blue", attrs=["bold"]
        )
    )
    verb31 = input(
        colored(
            "A verb:\n", "blue", attrs=["bold"]
        )
    )
    noun31 = input(
        colored(
            "A noun:\n", "blue", attrs=["bold"]
        )
    )

    if not all(x.isalpha() or x.isspace() for x in color31):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs03()
    elif not all(x.isalpha() or x.isspace() for x in adjective31): 
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs03()
    elif not all(x.isalpha() or x.isspace() for x in time31): 
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs03()
    elif not all(x.isalpha() or x.isspace() for x in adjective32): 
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs03()
    elif not all(x.isalpha() or x.isspace() for x in place31): 
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs03()
    elif not all(x.isalpha() or x.isspace() for x in food31): 
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs03()
    elif not all(x.isalpha() or x.isspace() for x in food32):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs03()
    elif not all(x.isalpha() or x.isspace() for x in verb31):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs03()
    elif not all(x.isalpha() or x.isspace() for x in noun31):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs03()
    else:
        madlibs3 = print(colored(
            f"Bats are {color31}, {adjective31} animals which have wings. " +
            f"They fly around at {time31} which scares people. " +
            f"Bats are {adjective32}. My pet bat lives at {place31}. " +
            f"I like to feed him {food31} and " +
            f"{food32}. He likes to {verb31}. " +
            f"I am his favorite person, but he also likes {noun31}. ",
            "yellow", attrs=["bold"])
        )
        continue_game()


def madlibs04():

    """
    Madlibs theme number 4
    """
    print(
        colored("Nursery Rhymes.",
                "light_yellow", attrs=["bold"])
    )

    adjective41 = input(
        colored(
            "An adjective:\n","light_yellow", attrs=["bold"]
        )
    )
    advedrb41 = input(
        colored(
            "An adverb:\n", "light_yellow", attrs=["bold"]
        )
    )
    adjective42 = input(
        colored(
            "Another adjective:\n", "light_yellow", attrs=["bold"]
        )
    )
    bodypart41 = input(
        colored(
            "Body part plural:\n", "light_yellow", attrs=["bold"]
        )
    )
    bodypart42 = input(
        colored(
            "Another body part plural:\n", "light_yellow", attrs=["bold"]
        )
    )

    if not all(x.isalpha() or x.isspace() for x in adjective41):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs04()
    elif not all(x.isalpha() or x.isspace() for x in advedrb41):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs04()
    elif not all(x.isalpha() or x.isspace() for x in adjective42):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs04()
    elif not all(x.isalpha() or x.isspace() for x in bodypart41):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs04()
    elif not all(x.isalpha() or x.isspace() for x in bodypart42):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs04()
    else:
        madlibs = print(colored(
            f"When some {adjective41} " +
            f"school students were asked what nursery " +
            f"rhymes popped {advedrb41} " +
            f"into their {adjective42} " +
            f"or were on the tip of their {bodypart41}" +
            f", these were their {bodypart42} answers:",
            "yellow", attrs=["bold"])
        )
        continue_game()


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
    elif selection == 4:
        madlibs04()
    elif selection == 5:
        madlibs05()
    elif selection == 6:
        madlibs06()
    else:
        print(
            colored("Invalid selection, please try again", "green")
        )
        main_choice()


def main():
    opening_function()


main()
