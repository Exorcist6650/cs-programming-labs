def main():
    user_input = str(input())

    print(f"""Длина: {len(user_input)}
Только буквы: {user_input.isalpha()}
Только цифры: {user_input.isdigit()}
Буквенно-цифровая: {user_input.isalnum()}
Содержит дефис: {'-' in user_input}""")

if __name__ == "__main__":
    main()

    