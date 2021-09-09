from math import sqrt

def carreparfait(n):
    return 'carré parfait' if sqrt(n) ** 2 == n else 'pas parfait'

def main():
    print(carreparfait(1))

if __name__ == '__main__':
    main()