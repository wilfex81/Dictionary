import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(words):
    words = words.lower()
    if words in data:
        return data[words]
    elif len(get_close_matches(words, data.keys())) > 0:
        yesno = input("Did you mean %s instead? Enter Y if yes, N if No: " %get_close_matches(words, data.keys())[0])
        if yesno == "Y":
            return data[get_close_matches(words, data.keys())[0]]
        elif yesno == "N":
            return "The word don't match, Please double check you word."
        else:
            return "Sorry, we could not find your word"
    else:
        return "The word does not exist. Please double check and try again"

word = input("Enter your word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
        
        
    
    