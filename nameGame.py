# Name Game: This program asks the user for their name and then prints out a name poem
# based on the user's name.
# Author: Sarah Perry


def main():
    # print welcome message
    print("\nWelcome to the Name Game! Enter your name and I will create a rhyme for you.")

    # get user input
    name = input("\nWhat is your name? ").strip().title()
    first_letter = name[0]

    # create rhyming variations
    if first_letter in "AEIOU":
        b_rhyme = 'b' + name.lower()
        f_rhyme = 'f' + name.lower()
        m_rhyme = 'm' + name.lower()

    elif first_letter in "BFM":
        b_rhyme = name[1:] if first_letter == 'B' else 'b' + name[1:]
        f_rhyme = name[1:] if first_letter == 'F' else 'f' + name[1:]
        m_rhyme = name[1:] if first_letter == 'M' else 'm' + name[1:]

    else:
        b_rhyme = 'b' + name[1:]
        f_rhyme = 'f' + name[1:]
        m_rhyme = 'm' + name[1:]

    # create rhyme
    rhyme = f"""
    {name}, {name}, bo-{b_rhyme}
    \nBanana-fana fo-{f_rhyme}
    \nFee-fi-mo-{m_rhyme}
    \n{name}!
    """

    # output rhyme
    print(rhyme)

    # print goodbye message
    print("\nThanks for playing the Name Game!\n")
    print("The Name Game is a song co-written and performed by Shirley Ellis & Lincoln Chase in 1964.")

if __name__ == "__main__":
    main()
