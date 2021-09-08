def main():
    print("Entrer 3 nombres")
    t = [int(input(">> ")) for _ in range(3)]
    print(f"maximum: {max(t)}")


if __name__ == '__main__':
    main()