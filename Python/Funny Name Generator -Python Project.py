import sys, random

print("Welcome to the Psych \'Sidekick Name Picker.\'\n")
print("A name just like Sean would pick for Gus: \n\n")

funny_first_names = ("Baby Oil", "Bad News", "Big Burps", "Bill 'Beenie-Weenie'", "Bob 'Stinkbug'", "Bowel Noises", "Butter Bean", "Buttermilk", "Booger Baby", "Stiny Leg", "Flex McGoogle", "Jimbo", "Cleet", "Clit", "Longshanks", "Tinfoil", "Herpes", "Dicman", "Cornbread", "Dennis 'Clawhammer'" )
funny_last_names =("Appleyard", "Bigmeat", "Bloominshine", "Clovenhoof", "Clutterbuck", "Cocktoasten", "Apricote", "Fewhairs", "Gooberapple", "Goodensnitch", "Jenkins", "Friskylegs", "Kingfish", "Olivetti", "Porkins", "Pennywhistle", "Quakenbush", "Vinaigrette", "Stroganoff", "Sackrider", "Snugglebuttle", "Splerm", "Turnipseed") 

while True:
    # choose a first name at random from list & assign to variable
    firstName = random.choice(funny_first_names)

    # choose a surname at random from list &Assign to a variable
    lastName = random.choice(funny_last_names)
    # print new funny name
    print("\n\n")
    print("{} {}".format(firstName, lastName), file=sys.stderr)
    print("\n\n")
    #ask user if he wants to play again
    try_again = input("\n\n Try again? (Press Enter else n to quit)\n ")
    # if yes: run program again
    if try_again.lower() == "n":
     break
    #if no: exit
input("\n Press Enter to exit.")