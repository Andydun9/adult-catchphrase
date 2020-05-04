import json
import random

data = json.load(open("data.json", "r"))
wtf = json.load(open("wtf.json", "r"))
# categories: "What Mom Found in my Bedroom"
# what the fuck did you do to the cat?

def phrases(userInput): 
    return data[random.randrange(0,2)]

def phrases2(userInput): 
    return wtf[random.randrange(0,2)]

userInput= input("Select Your Category: ")

if userInput == "What Mom Found in my Bedroom":
    print(phrases(userInput))
elif userInput == "what the fuck did you do to the cat?":
    print(phrases2(userInput))
