def main():
    user_input = str(input())

    category, year, number = user_input.split('-')

    print(f"""Категория: {category}
Год: {year}
Номер: {number}
Обратный номер: {number[::-1]}""")

if __name__ == "__main__":
    main()
