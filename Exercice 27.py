class Calcule:
    def __init__(self, x):
        self.x = x

    def add(self):
        return sum(self.x)

    def mult(self):
        m = 1

        for x in self.x:
            m *= x
        return m



def main():
    print('Entrer 5 nombres')
    t = [int(input(">> ")) for _ in range(5)]
    print(f'Multiplication: {Calcule(t).mult()}')
    print(f'Addition: {Calcule(t).add()}')



if __name__ == '__main__':
    main()