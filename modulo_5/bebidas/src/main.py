import re


def validateName(name): # receives a String
    alphabetic = re.search("[^a-zA-Z]",name) is None
    length = len(name) >= 2 and len(name) <= 15
    return alphabetic and length


def validateSize(sizeArray): # receives a List of Strings
    numeric = re.search(r"\D",''.join(sizeArray)) is None
    if not numeric:
        return False
    length = len(sizeArray) >= 1 and len(sizeArray) <= 5
    order = sizeArray == sorted(sizeArray)
    sizeValues = list(map(lambda x: int(x), sizeArray))
    sizeRange = min(sizeValues) >= 1 and max(sizeValues) <= 48
    nonduplicate = len(sizeArray) == len(set(sizeArray))
    return length and order and sizeRange and nonduplicate


def validateString(string): # receives a String
    input = string.replace(' ','').split(',')
    if len(input) < 2 or not validateName(input[0]):
        return False
    return True

if __name__ == '__main__':
    drink = input('> ')
    if validateString:
        print('Bebida añadida con éxito')
    else:
        print('Ingrese una entrada válida')
