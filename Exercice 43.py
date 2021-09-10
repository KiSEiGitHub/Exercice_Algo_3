def InsertEtoile(x):

    nouvelle_chaine = ""

    for i in x:
        nouvelle_chaine += i + "*"
    
    return nouvelle_chaine


def main():
    c = input('Entrer un chaine: ')
    print(InsertEtoile(c))

if __name__ == '__main__':
    main()