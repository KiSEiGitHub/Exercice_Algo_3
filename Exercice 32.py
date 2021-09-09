import itertools


def main():
    l = [1, 2, 3, 4]
    permutations = itertools.permutations(l)
    L = list(permutations)
    print("Les listes obtenues en échangeant les termes de la liste l:\n", L)


if __name__ == '__main__':
    main()