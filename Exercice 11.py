def main():
    div = []

    n = int(input("n: "))

    for i in range(1, n + 1):
        if n % i == 0:
            div.append(i)
    
    print(div)


if __name__ == '__main__':
    main()