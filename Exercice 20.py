def main():
    s = "coucou"
    n = len(s)

    first = s[0]
    last = s[n - 1]

    s1 = s[1:n - 1]

    s2 = last + s1 + first
    print(s2)


if __name__ == '__main__':
    main()