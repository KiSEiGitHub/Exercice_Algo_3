def nombreMajscule(chaine):
    nb_minuscule = 0
    nb_majuscule = 0

    for lettre in chaine:
        if lettre.isupper():
            nb_majuscule += 1

        elif lettre.islower():
            nb_minuscule += 1
    
    return nb_minuscule, nb_majuscule


def main():

    n = input('Entrer chaine: ')
    l_min, l_maj = nombreMajscule(n)
    
    print(f'Nombre de minuscule: {l_min}')
    print(f'Nombre de majuscule: {l_maj}')

if __name__ == '__main__':
    main()