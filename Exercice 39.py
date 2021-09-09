def main():
    chaine = input('Entrer une chaine: ')
    a = chaine.split()
    nb_mot = len(a)

    print(f'nombre de mot: {nb_mot}')


if __name__ == '__main__':
    main()