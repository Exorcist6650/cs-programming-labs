def main():
    purchases_count = 0
    total_cost = 0

    while True:
        user_input = input()

        if user_input == "stop":
            break

        purchase_cost = int(user_input)

        if not(purchase_cost > 0):
            raise ValueError("Not valid value")

        purchases_count += 1
        total_cost += purchase_cost

    if purchases_count == 0:
        print("Нет покупок")

    else:
        average = total_cost / purchases_count
        print(f"Покупок: {purchases_count}")
        print(f"Общая стоимость: {total_cost} руб")
        print(f"Средняя стоимость: {average:.2f} руб")

if __name__ == "__main__":
    main()