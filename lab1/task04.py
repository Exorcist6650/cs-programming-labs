def main():
    input_seconds = int(input())

    hours, remainder = divmod(input_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')

if __name__ == "__main__":
    main()

