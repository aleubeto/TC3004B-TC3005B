import re


def newDrink(drink):
    return drink.split(',')


def validateName(name):
    alphabetic = len(re.findall("[^a-zA-Z]",name)) == 0
    length = len(name) >= 2 and len(name) <= 15
    return alphabetic and length


def validateSize():
    return 0