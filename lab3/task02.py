def main():
    user_input = str(input())

    surname, name, patronymic = user_input.split()

    print(f'{surname.title()} {name[0].upper()}. {patronymic[0].upper()}.')

if __name__ == "__main__":
    main()
    