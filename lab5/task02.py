
def main():
    a = int(input())
    b = int(input())

    if not(a <= b): 
        raise ValueError("Not valid number")

    summary = 0
    multiplication = 1

    for i in range(a, b + 1):
        summary += i
        multiplication *= i

    print(f"Сумма: {summary}")
    print(f"Произведение: {multiplication}")

if __name__ == "__main__":
    main()