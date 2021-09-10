def MotCommuns(m, m1):

    l_1 = m.split()
    l_2 = m1.split()

    mot = []

    for a in l_1:
        if a in l_2:
            mot.append(a)
    
    return mot

def main():
    chaine = "Python est un langage de programmation"  
    chaine_2 = "Python est orienté objet"

    print(f'Mot communs: {MotCommuns(chaine, chaine_2)}')


if __name__ == '__main__':
    main()