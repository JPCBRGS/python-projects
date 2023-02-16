from difflib import SequenceMatcher, get_close_matches
import json

data = json.load(open("data.json"))

def translate (word):
    word = word.lower()
    if word in data:
        return data[word]
    
    elif len(get_close_matches("word", data.keys()))>0:
        yn = input("Typed word not found, did you mean %s instead? Enter Y for YES or N for NO: " % get_close_matches(word, data.keys())[0])
        if yn.lower() == 'y':
            return data[get_close_matches("word", data.keys(), [0])]
        elif yn.lower() == 'n':
            return "Word not found."
        else:
            return "Couldn't understand entry."

    else:
        return "Word not found."

word = input("Enter a word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)