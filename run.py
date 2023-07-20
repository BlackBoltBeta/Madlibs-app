import sys

from termcolor import colored, cprint

# This variable works with the continue_game function
afirm = "yes"

theme_one = "1"
theme_two = "2"
theme_three = "3"
theme_four = "4"
theme_five = "5"


def opening_function():

    """
    This is the welcome message and the instructions
    """
    print(colored(
            "Welcome to Llama Madlibs.\n" +
            "First select a theme for your mad libs, " +
            "and then fill out the prompts with random words.\n" +
            "When the text is complete you can read it out loud!"
            , "blue", attrs=["bold"]))
    print(colored(
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
    print(colored(
        "Type 4 for Nursery Rhymes.\n",
        "yellow", attrs=["bold"]))
    print(colored(
        "Type 5 for BIRTHDAY PARTY FUN!.\n",
        "red", attrs=["bold"]))
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
    print(colored(
        "Type 4 for Nursery Rhymes.\n",
        "yellow", attrs=["bold"]))
    print(colored(
        "Type 5 for BIRTHDAY PARTY FUN!.\n",
        "red", attrs=["bold"]))
    main_choice()


def continue_game():

    """
    This function asks the player if they wish to continue,
    and restarts the game if they input "yes"
    """

    continue_quest = input(colored(
        "To play again please type 'yes', any other key will end the game:\n",
        "magenta", attrs=["reverse", "blink"]
    ))

    if continue_quest.lower() == afirm:
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


    if (len(adjective11) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs01()
    elif (len(plural_nou11) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs01()
    elif (len(plural_nou12) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs01()
    elif (len(plural_nou13) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs01()
    elif (len(plural_nou14) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs01()
    elif (len(adverb11) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs01()
    elif (len(noun11) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs01()
    elif (len(noun12) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs01()
    elif not all(x.isalpha() or x.isspace() for x in adjective11):
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

    if (len(adjective21) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif (len(adjective22) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif (len(adjective23) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif (len(adjective24) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif (len(adjective25) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif (len(place21) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif (len(pieceofcloth21) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif (len(bodypart21) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif (len(bodypart22) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif (len(bodypart23) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif (len(noun21) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif (len(noun22) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif (len(place22) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs02()
    elif not all(x.isalpha() or x.isspace() for x in adjective21):
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

    if (len(color31) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs03()
    elif (len(adjective31) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs03()
    elif (len(time31) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs03()
    elif (len(adjective32) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs03()
    elif (len(place31) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs03()
    elif (len(food31) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs03()
    elif (len(food32) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs03()
    elif (len(verb31) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs03()
    elif (len(noun31) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs03()
    elif not all(x.isalpha() or x.isspace() for x in color31):
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
            "An adjective:\n", "light_yellow", attrs=["bold"]
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

    if (len(adjective41) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs04()
    elif (len(advedrb41) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs04()
    elif (len(adjective42) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs04()
    elif (len(bodypart41) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs04()
    elif (len(bodypart42) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs04()
    elif not all(x.isalpha() or x.isspace() for x in adjective41):
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


def madlibs05():

    """
    Madlibs theme number 5
    """
    print(
        colored("BIRTHDAY PARTY FUN!.",
                "light_yellow", attrs=["bold"])
    )

    pers_name51 = input(
        colored(
            "A person's name:\n", "light_yellow", attrs=["bold"]
        )
    )
    noun51 = input(
        colored(
            "An noun:\n", "light_yellow", attrs=["bold"]
        )
    )
    adjective51 = input(
        colored(
            "An adjective:\n", "light_yellow", attrs=["bold"]
        )
    )
    activity51 = input(
        colored(
            "An activity:\n", "light_yellow", attrs=["bold"]
        )
    )
    verb51 = input(
        colored(
            "A verb:\n", "light_yellow", attrs=["bold"]
        )
    )
    pers_name52 = input(
        colored(
            "A peron's name:\n", "light_yellow", attrs=["bold"]
        )
    )
    noun52 = input(
        colored(
            "A noun:\n", "light_yellow", attrs=["bold"]
        )
    )
    pers_name53 = input(
        colored(
            "A person's name:\n", "light_yellow", attrs=["bold"]
        )
    )
    noun53 = input(
        colored(
            "A noun:\n", "light_yellow", attrs=["bold"]
        )
    )
    past_tense_verb51 = input(
        colored(
            "A past tense verb:\n", "light_yellow", attrs=["bold"]
        )
    )
    song_name51 = input(
        colored(
            "The name of a song:\n", "light_yellow", attrs=["bold"]
        )
    )
    adjective52 = input(
        colored(
            "An adjective:\n", "light_yellow", attrs=["bold"]
        )
    )
    pers_name54 = input(
        colored(
            "A perosn's name:\n", "light_yellow", attrs=["bold"]
        )
    )
    activity52 = input(
        colored(
            "An activity:\n", "light_yellow", attrs=["bold"]
        )
    )

    if (len(pers_name51) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif (len(noun51) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif (len(noun52) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif (len(adjective51) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif (len(activity51) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif (len(verb51) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif (len(pers_name52) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif (len(noun53) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif (len(past_tense_verb51) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif (len(song_name51) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif (len(adjective52) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif (len(pers_name54) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif (len(activity52) == 0):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif not all(x.isalpha() or x.isspace() for x in pers_name51):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif not all(x.isalpha() or x.isspace() for x in noun51):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif not all(x.isalpha() or x.isspace() for x in adjective51):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif not all(x.isalpha() or x.isspace() for x in activity51):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif not all(x.isalpha() or x.isspace() for x in verb51):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif not all(x.isalpha() or x.isspace() for x in pers_name52):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif not all(x.isalpha() or x.isspace() for x in noun52):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif not all(x.isalpha() or x.isspace() for x in pers_name53):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif not all(x.isalpha() or x.isspace() for x in noun53):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif not all(x.isalpha() or x.isspace() for x in past_tense_verb51):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif not all(x.isalpha() or x.isspace() for x in song_name51):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif not all(x.isalpha() or x.isspace() for x in adjective52):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif not all(x.isalpha() or x.isspace() for x in pers_name54):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    elif not all(x.isalpha() or x.isspace() for x in activity52):
        print(colored(
            "Please make sure you type words only.", "red", attrs=["bold"]))
        madlibs05()
    else:
        madlibs = print(colored(
            f"Yesterday I went to  {pers_name51}'s" +
            f"birthday party. I got them a {noun51}. " +
            f"The party was {adjective51}. " +
            f"We started by playing {activity51}" +
            f"and then there was a {verb51} party. " +
            f"Lots of my friends were there" +
            f"but I mostly hung out with {pers_name52}. " +
            f"We talked about {noun52} and " +
            f"how our friend {pers_name53} is a {noun53}. " +
            f"During cake everyone {past_tense_verb51}" +
            f"and sang  {song_name51}. I had a {adjective52}" +
            f"time at the party and enjoyed celebrating {pers_name54}. " +
            f"He/she is such a {activity52} friend.",
            "yellow", attrs=["bold"])
        )
        continue_game()


def main_choice():
    selection = input(
        colored(
            "select your theme:\n", "blue", attrs=["reverse", "blink"]
        )
    )

    """
    This function allows the user to select a theme
    """
    if selection is theme_one:
        madlibs01()
    elif selection is theme_two:
        madlibs02()
    elif selection is theme_three:
        madlibs03()
    elif selection is theme_four:
        madlibs04()
    elif selection is theme_five:
        madlibs05()
    else:
        print(
            colored("Invalid selection, please try again", "green")
        )
        main_choice()


def main():
    opening_function()


main()
