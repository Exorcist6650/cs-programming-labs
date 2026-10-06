def main():
    year = int(input())

    if not(1 <= year <= 9999):
        print('Ошибка')

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print('Високосный')
    else:
        print('Невисокосный')

if __name__ == "__main__":
    main()