# importing the random module
import random

def rand(min, max):
    return random.randint(min, max)

def app(money):
    number = None
    if(rand(0, 2) == 0):
        number = rand(0,10) / 10
    else:
        number = rand(0, 15) / 10
    print(money * number)

app(10)