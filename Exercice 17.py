def main():
    s = 'Hello World'
    occu =set({})

    for l in s:
        if l not in occu:
            occu.add(l)
            print(f"Nombre d'occurence de {l} est {s.count(l)}")


if __name__ == '__main__':
    main()