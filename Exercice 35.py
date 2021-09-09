def main():
    url = input("url: ")
    lien = input("lien: ")

    url = "<a href='"+ url + "'> " + lien + "</a>"

    print(url)

if __name__ == '__main__':
    main()