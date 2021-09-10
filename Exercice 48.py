def lettre(s):

    if len(s) == 0:
        return True
    elif s[0] == s[-1]:
        return True
    else:
        return False

def main():

    print(lettre("render")) 
    print(lettre("Python"))  

if __name__ == '__main__':
    main()