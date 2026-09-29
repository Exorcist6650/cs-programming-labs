def main():
    user_input = str(input())

    train_number, from_place, to_place, time, price = user_input.split(';')

    print(f"""Поезд: {train_number}
Маршрут: {from_place} - {to_place}
Отправление: {time}
Цена: {float(price):.2f} руб""")

if __name__ == "__main__":
    main()

