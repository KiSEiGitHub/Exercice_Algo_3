def palindrome(mot):
    return f'{mot} est un palindrome' if mot == mot[::-1] else f"{mot} n'est pas un palindrome"

def main():
    n = input("mot: ")
    print(palindrome(n))


if __name__ == '__main__':
    main()