def main():
    while True:
        try:
            v = {'a', 'e', 'y', 'u', 'i', 'o'}
            n = input("Entrer mot: ")

            flag = sum(n[i] in v for i in range(len(v)))

            print(f"Nombre de voyelles dans {n}: {flag}")

            break
        except IndexError:
            print('Une erreur est survenue')

if __name__ == '__main__':
    main()