def main():
    n = int(input("n: "))
    factorielle = 1

    for i in range(1, n + 1):
        factorielle *= i

    print(f"Factorielle de {n}: {factorielle}")


if __name__ == '__main__':
    main()