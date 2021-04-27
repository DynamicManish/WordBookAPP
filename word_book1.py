import json 
import time 
from difflib import get_close_matches as gc

get_keys = json.load(open("wordbook.json"))

def find_meaning(user_word):
    if user_word.lower() in get_keys:
        return get_keys[user_word.lower()]
    elif user_word.upper() in get_keys:
        return get_keys[user_word.upper()]
    elif user_word.title() in get_keys:
        return get_keys[user_word.title()]
    elif len(gc(user_word.lower(),get_keys.keys())) > 0:
        close_matches = (gc(user_word.lower(),get_keys.keys())[0])     
        user_decision = input(
            "🤔 Are you looking for "+"'"+close_matches+"'"+" instead of"+"'"+user_word.lower()+"'"+"❓[Y/N]: ")
        if user_decision.strip().lower() == "y":
            return get_keys[close_matches]
        elif user_decision.strip().lower() == "n":
            print("⚠️ " + "Can't find word, Please check the spelling❗")
        else:
            print("Invalid Input❗❗")      
    elif len(gc(user_word.upper(), get_keys.keys())) > 0:
        close_matches = (gc(user_word.upper(), get_keys.keys())[0])
        user_decision = input(
            "🤔 Are you looking for "+"'"+close_matches+"'"+" instead of"+"'"+user_word.upper()+"'"+"❓[Y/N]: ")
        if user_decision.strip().lower() == "y":
            return get_keys[close_matches]
        elif user_decision.strip().lower() == "n":
            print("⚠️ " + "Can't find word, Please check the spelling❗")
        else:
            print("Invalid Input❗❗")
    elif len(gc(user_word.title(), get_keys.keys())) > 0:
        close_matches = (gc(user_word.title(), get_keys.keys())[0])
        user_decision = input(
            "🤔 Are you looking for "+"'"+close_matches+"'"+" instead of"+"'"+user_word.title()+"'"+"❓[Y/N]: ")
        if user_decision.strip().lower() == "y":
            return get_keys[close_matches]
        elif user_decision.strip().lower() == "n":
            print("⚠️ " + "Can't find word, Please check the spelling❗")
        else:
            print("Invalid Input❗❗")
    else:
        print("❌ Sorry, I can't find meaning")

user_word = str(input("🚀 Type word to find it's meaning: ")).strip()
output = find_meaning(user_word)

if type(output) == list:
    for word_meanings in output:
        print("🔹 "+word_meanings)
else:
    None  
