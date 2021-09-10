def nombreOccurences(list, x):
    occurence = 0

    for element in list:
        if element == x:
            occurence += 1

    return occurence

def main():

    l = [1, 2, 3, 3, 2, 5, 5, 2, 1, 89, 0]
    var = nombreOccurences(l, 3)
    print(f"Nombre d'occurence de 1: {var}")

if __name__ == '__main__':
    main()