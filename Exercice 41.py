def nombre_Divisibles(l, n):
    i = 0
    for k in l:
        if k % n == 0:
            i += 1
        return i

def main():
    liste = [1, 2, 3, 4, 5]
    n = 8

    print(f'il y a {nombre_Divisibles(liste, n)} nombre divible par {n}')


if __name__ == '__main__':
    main()