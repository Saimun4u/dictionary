import json

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
    else:
        return 'The word is not in the dictionary'

word = input('Enter the meaning of the word you want to search: ')


# for w, m in data.items():
#     if word == w:
#         print(translate(word))
# print('The word is not in the dictionary')

print(translate(word))



