def main():
    user_input = str(input())

    user_path = '/'.join(user_input.split(','))

    print(user_path)

if __name__ == "__main__":
    main()

    