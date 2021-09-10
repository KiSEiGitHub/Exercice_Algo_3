def toutEnMajuscule(l):
    liste_maj = []

    for i in l:
        liste_maj.append(i.upper())
    
    return liste_maj

def main():
    l = ['salut', 'coucou']
    print(toutEnMajuscule(l))

if __name__ == '__main__':
    main()