def main():
    triangle_size = int(input())
    odd_counter = 0

    for column in range(triangle_size):

        current_value = 1

        for row in range(column + 1):

            if current_value % 2 != 0:
                odd_counter += 1
            
            if row == column:
                print(current_value)

            else:
                print(current_value, end=" ")
            
            current_value = current_value * (column - row) // (row + 1)

    print(f"Нечетных элементов: {odd_counter}")

if __name__ == "__main__":
    main()