def main():
    number = int(input())

    if not(number > 0):
        raise ValueError("Not valid value")

    for i in range(number, -1, -1):
        print(i)

if __name__ == "__main__":
    main()