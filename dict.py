import json
import difflib
from difflib import get_close_matches

data = json.load(open('data.json'))


#My solution

# def take_input():
#
#     while True:
#
#         word = input('\n Enter the word you want to search: ')
#         print("To try another word, enter 'y' or else 'n' to quit")
#
#         for w, m in data.items():
#             if word == w:
#                 print(data[w])
#
#         if word == 'n':
#             print('Thanks for using the dictionary')
#             break
#
#             # elif word != w:
#             #     print(f'The word {word} cannot be found in the dictionary')
#
# take_input()


#Ardit's solution

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        user_response = input(f'Did you mean the word {get_close_matches(w, data.keys())[0]}. Enter y for yes and n for no: ')
        if user_response == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif user_response == 'n':
            return "The word is not found in the dictionary"
        else:
            return "Please enter y or n only"
    else:
        return 'The word is not in the dictionary'


word = input('Enter the meaning of the word you want to search: ')


# for w, m in data.items():
#     if word == w:
#         print(translate(word))
# print('The word is not in the dictionary')

meaning = translate(word)


if type(meaning) == list:
    for option in meaning:
        print(option)
else:
    print(meaning)




