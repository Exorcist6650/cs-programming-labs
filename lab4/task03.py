def main():
    x = float(input())
    y = float(input())

    # Position compute
    result_position :str = ''
    if x != 0 and y == 0:
        result_position = 'Ось X'
    elif x == 0 and y != 0:
        result_position = 'Ось Y'
    elif x > 0 and y > 0:
        result_position = 'I четверть'
    elif x < 0 and y > 0:
        result_position = 'II четверть'
    elif x < 0 and y < 0:
        result_position = 'III четверть'
    elif x > 0 and y < 0:
        result_position = 'IV четверть'
    else:
        result_position = 'Начало координат'

    print(result_position)

if __name__ == "__main__":
    main()