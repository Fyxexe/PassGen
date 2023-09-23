import random
import string
import json
import os

def PassGen(symbolCount):
    symbols = string.ascii_letters + string.digits 
    password = []

    for _ in range(symbolCount):
        random_symbol = random.choice(symbols)
        password.append(random_symbol)

    return ''.join(password)

def repeat(data):
    while True:
        repeatGen = input('Change your password [y/n]: ')

        if repeatGen == "y":
            symbolCount = int(input("Input symbol count: "))
            password = PassGen(symbolCount)
            print(password)
            data.append(password)  
        elif repeatGen == "n":
            break
        else:
            print("Invalid input")


data_file = 'data/data.json'

if os.path.exists(data_file):
    with open(data_file, 'r') as file:
        data = json.load(file)
else:
    data = []

if not isinstance(data, list):
    data = []

symbolCount = int(input("Input symbol count: "))
password = PassGen(symbolCount)
data.append(password)

with open(data_file, 'w') as file:
    json.dump(data, file, indent=4)

print(password)


repeat(data)


with open(data_file, 'w') as file:
    json.dump(data, file, indent=4)
