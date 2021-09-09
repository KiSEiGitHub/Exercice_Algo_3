def premier(n):
    i = 2
    while i < n and n % i != 0:
        i += 1
    if i == n:
        print(f'{n} est un nombre premier')
    else:
        print(f"{n} n'est pas premier")

def main():
    premier(242)

if __name__ == '__main__':
    main()