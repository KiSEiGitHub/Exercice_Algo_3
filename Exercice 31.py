def main():
    l = [2, 5, 4, 525, 35, 321, 376, 2, 6, 29, 230]
    pair = []
    impair = []

    for i in l:
        if i % 2 == 0:
            pair.append(i)
        else:
            impair.append(i)

    print(f'pair: {pair}')
    print(f'impair: {impair}')


if __name__ == '__main__':
    main()