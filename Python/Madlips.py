# #string concatenation (aka how to put strings together)
# #suppose whe want to create a string that says "subscribe to ___"
# youtuber = "Total Biscuit" #some string variable

# # few ways to do this:
# print("subscribe to " + youtuber)
# #or
# print('subscribe to {}'.format(youtuber))
# #or
# print(f"subscribe to {youtuber}")

# A madlib generator in Python

adj = input("Adjective: ")
verb1 =input("verb 1: ")
verb2 = input("verb2: ")
famous_person = input("Famous Person: ")
madlib =f"Computer programming is so {adj}! It makes me so excited all the time because \
    I love to {verb1} and {verb2}. Stay hydrated like you are {famous_person}!"
print(madlib)