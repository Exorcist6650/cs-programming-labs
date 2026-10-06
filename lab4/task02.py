def main():
    base_price = float(input())
    passenger_age = float(input())

    # Age condition
    if not(0 <= passenger_age <= 120):
        print('Ошибка')

    # Individual price compute
    individual_price :float = 0.0

    if 0 <= passenger_age <= 5:
        individual_price = 0.0
    elif 6 <= passenger_age <= 17:
        individual_price = base_price / 100 * 50
    elif 60 <= passenger_age <= 120:
            individual_price = base_price / 100 * 70
    else: 
        individual_price = base_price

    print(f'Стоимость: {individual_price:.2f} руб')

if __name__ == "__main__":
    main()