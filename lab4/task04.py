def main():
    side_1 = int(input())
    side_2 = int(input())
    side_3 = int(input())

    error_text = 'Треугольник не существует'

    # Sides checking
    for side in (side_1, side_2, side_3):
        if side < 0:
            print(error_text)

    if (side_1 + side_2 <= side_3
        or side_1 + side_3 <= side_2
        or side_2 + side_3 <= side_1):

        print(error_text)

    # Compute triangle type
    sides_unique = len({side_1, side_2, side_3})
    match sides_unique:
        case 1:
            print('Равносторонний')
        case 2:
            print('Равнобедренный')
        case _ :
            print('Разносторонний')

if __name__ == "__main__":
    main()