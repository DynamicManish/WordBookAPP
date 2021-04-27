import json 
import time  
from difflib import get_close_matches as gm

elements = json.load(open("wordbook.json"))
def find_meaning(word):
    if word.lower() in elements:
        return elements[word.lower()]
    elif word.upper() in elements:
        return elements[word.upper()]
    elif word.title() in elements:
        return elements[word.title()]    
    elif word.lower() not in elements:
        try:
            print("Did you mean "+"'"+gm(word.lower(),elements.keys())[0]+"'"+" instead of "+"'"+word.lower()+"'"+"❓")  
            user_decision = input("[Y/N]: ").strip().lower()
        except:
            print("Sorry, I can't find your word")
        if user_decision == "y":
            for word_meanings in elements[gm(word.lower(), elements.keys())[0]]:
                print("🔸 "+word_meanings)
        elif user_decision == "n":
            print("⚠️ "+ "Can't find word, Please check the spelling❗")
            exit()
        else:
            print("Invalid Input❗❗")   
    elif word.upper() not in elements:
        try:
            print("Did you mean "+"'"+gm(word.upper(), elements.keys())
                  [0]+"'"+" instead of "+"'"+word.upper()+"'"+"❓")
            user_decision = input("[Y/N]: ").strip().lower()
        except:
            print("Sorry, I can't find your word")
        if user_decision == "y":
            for word_meanings in elements[gm(word.upper(), elements.keys())[0]]:
                print("🔸 "+word_meanings)
        elif user_decision == "n":
            print("⚠️ " + "Can't find word, Please check the spelling❗")
            exit()
        else:
            print("Invalid Input❗❗")
    elif word.title() not in elements:
        try:
            print("Did you mean "+"'"+gm(word.title(), elements.keys())
                  [0]+"'"+" instead of "+"'"+word.title()+"'"+"❓")
            user_decision = input("[Y/N]: ").strip().lower()
        except:
            print("Sorry, I can't find your word")
        if user_decision == "y":
            for word_meanings in elements[gm(word.title(), elements.keys())[0]]:
                print("🔸 "+word_meanings)
        elif user_decision == "n":
            print("⚠️ " + "Can't find word, Please check the spelling❗")
            exit()
        else:
            print("Invalid Input❗❗")
word = str(input("Type word here: ")).strip()
time.sleep(1)

try:
    if type(find_meaning(word)) == list:
        for word_meanings in find_meaning(word):
            print("🔸 "+word_meanings)
except:
    None    
