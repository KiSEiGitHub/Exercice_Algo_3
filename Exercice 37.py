def main():
    chaine_1 = input('Entrer chaine: ')
    chaine_2 = input('Entrer chaine: ')

    liste_1 = chaine_1.split()
    liste_2 = chaine_2.split()

    liste_commune = [i for i in liste_1 if i in liste_2]

    print(liste_commune)


if __name__ == '__main__':
    main()