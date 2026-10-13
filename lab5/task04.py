def main():
    number = int(input())

    if not(1 <= number <= 9):
        raise ValueError("Not valid value")
        
    multiplicand = number
    for multiplier in range(1, 10 + 1):
        print(f"{multiplicand} * {multiplier} = "
              f"{multiplicand * multiplier}")

if __name__ == "__main__":
    main()