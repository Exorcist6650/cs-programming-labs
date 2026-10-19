
def main():
    n = int(input())

    if not(n > 0): 
        raise ValueError("Not valid value")
        
    below_zero = 0
    equal_zero = 0
    above_zero = 0

    for _ in range(n):
        temp = float(input())
        if temp < 0:
            below_zero += 1
        elif temp > 0:
            above_zero += 1
        else:
            equal_zero += 1

    print(f"Ниже нуля: {below_zero}")
    print(f"Равны нулю: {equal_zero}")
    print(f"Выше нуля: {above_zero}")

if __name__ == "__main__":
    main()