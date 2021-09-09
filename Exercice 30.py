def elementsCommun(l1,l2):
    compteur = sum(x in l2 for x in l1)
    return compteur != 0


def main():
    l1 = [2, 278, 590, 25, 28]
    l2 = [2, 25, 58, 298, 19]
    print(elementsCommun(l1, l2))


if __name__ == '__main__':
    main()