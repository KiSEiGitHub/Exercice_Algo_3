def main():
    s = "Apprendre Python sur www.tresfacile.net"

    premierMot = ""

    i = 0

    while s[i] != " ":
        premierMot += s[i]
        i += 1
    print("Le premier mot de la chaine s est  : ", s[:i])


if __name__ == '__main__':
    main()