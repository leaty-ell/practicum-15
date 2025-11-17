def function1(x, divisor) -> int:
    """
    Recursive function to check if number is prime.
    
    Args:
        x (int): Natural number to check
        divisor (int): Current divisor (for recursion)
        
    Returns:
        int: 1 if prime, 0 if composite
    """
    if x < 2:
        return 0
    if x == 2:
        return 1
    if divisor * divisor > x:
        return 1
    if x % divisor == 0:
        return 0
    
    return function1(x, divisor + 1)


def main():
    """
    Main function to get input from keyboard
    """
    x = int(input("Введите натуральное число: "))
    
    result = function1(x)
    if result == 1:
        print(f"Число {x} является простым")
    else:
        print(f"Число {x} не является простым")


if __name__ == "__main__":
    main()
