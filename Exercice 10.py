from math import pi


class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def surface(self):
        return pi * self.rayon ** 2

    def perimetre(self):
        return 2 * pi * self.rayon


def main():
    rayon = Cercle(7)

    print(f'Surface = {round(rayon.surface(), 2)}')
    print(f'Périmètre = {round(rayon.perimetre(), 2)}')


if __name__ == '__main__':
    main()