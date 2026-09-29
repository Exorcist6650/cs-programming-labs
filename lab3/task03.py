def main():
    user_input = str(input())

    telephone_number = user_input

    #Replacing all symbols
    for symbol in "+()- ":
        telephone_number = telephone_number.replace(symbol, '')

    print(telephone_number)

if __name__ == "__main__":
    main()

