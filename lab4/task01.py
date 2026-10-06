def main():
    current_temp = float(input())
    new_temp = float(input())

    # Command compute
    result_command :str = ''
    if current_temp < new_temp:
        result_command = 'Нагрев'
    elif current_temp > new_temp:
        result_command = 'Охлаждение'
    else:
        result_command = 'Выключен'

    print(result_command)

if __name__ == "__main__":
    main()