def ch(s):
    a = s.split()

    mot_le_plus_long = ""

    for i in a:
        if len(i) > len(mot_le_plus_long):
            mot_le_plus_long = i

    return mot_le_plus_long

def main():
    chaine = input('Entrer chaine: ')

    print(f'Mot le plus long: {ch(chaine)}')


if __name__ == '__main__':
    main()