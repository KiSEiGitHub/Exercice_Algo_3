def main():

    chaine = input("Chaine: ")
    chaine_ = "".join(chaine[i] for i in range(0, len(chaine) - 1, 2))
    print(chaine_)


if __name__ == '__main__':
    main()