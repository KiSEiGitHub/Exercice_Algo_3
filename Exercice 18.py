def main():
    chaine = input("Entrer une chaine: ")

    for i in range(len(chaine)):
        if chaine[i] == 'a':
            print(f"Le caractère a se trouve a la potition {i}")
            break
        else:
            print('Pas de a')

if __name__ == '__main__':
    main()