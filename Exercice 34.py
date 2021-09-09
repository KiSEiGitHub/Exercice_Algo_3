def main():
    notes = [12 , 4 , 14 , 11 ,  18 , 13 ,  7, 10 , 5 , 9 , 15 , 8 , 14 , 16]
    note_au_dessus_de_10 = [i for i in notes if i >= 10]

    print(note_au_dessus_de_10)

if __name__ == '__main__':
    main()