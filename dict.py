import json

data = json.load(open('data.json'))


def take_input():

    while True:

        word = input('Enter the word you want to search: ')

        for w, m in data.items():
            if word == w:
                print(data[w])

            # elif word != w:
            #     print(f'The word {word} cannot be found in the dictionary')

take_input()
