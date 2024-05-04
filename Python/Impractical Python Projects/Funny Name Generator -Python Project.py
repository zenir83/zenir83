import sys
import random

def main():
    """Choose names at random from two tuples of names and print on screen"""
    print("Welcome to the Psych \'Sidekick Name Picker.\'\n")
    print("A name just like Sean would pick for Gus: \n\n")

    first = ("Baby Oil", "Bad News", "Big Burps", "Bill 'Beenie-Weenie'", "Bob 'Stinkbug'", "Bowel Noises", "Butter Bean", "Buttermilk", "Booger Baby", "Stiny Leg", "Flex McGoogle", "Jimbo", "Cleet", "Clit", "Longshanks", "Tinfoil", "Herpes", "Dicman", "Cornbread", "Dennis 'Clawhammer'")
    last =("Appleyard", "Bigmeat", "Bloominshine", "Clovenhoof", "Clutterbuck", "Cocktoasten", "Apricote", "Fewhairs", "Gooberapple", "Goodensnitch", "Jenkins", "Friskylegs", "Kingfish", "Olivetti", "Porkins", "Pennywhistle", "Quakenbush", "Vinaigrette", "Stroganoff", "Sackrider", "Snugglebuttle", "Splerm", "Turnipseed") 

    while True:
        # choose a first name at random from list & assign to variable
        first_name = random.choice(first)

        # choose a surname at random from list &Assign to a variable
        last_name = random.choice(last)
        # print new funny name
        print("\n\n") 
        #Trick IDLE by using "fatal error" setting to print the name in red(doesn't work for VSCode)
        print("{} {}".format(first_name, last_name), file=sys.stderr)
        print("\n\n")
        #ask user if he wants to play again
        try_again = input("\n\n Try again? (Press Enter else n to quit)\n ")
        # if yes: run program again
        if try_again.lower() == "n":
            break
        #if no: exit
    
    
    input("\n Press Enter to exit.")

if __name__ == "__main__":
    main()