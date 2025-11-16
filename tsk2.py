def count(n) -> int:
    """
    Recursive function to count the number of digits in a natural number.
    
    Args:
        n (int): Natural number
    
    Returns:
        int: Number of digits in the number
    """
    if n < 10:
        return 1
    else:
        return 1 + count(n // 10)


def main():
    """
    Main function to get input from keyboard
    """
    n = int(input("Введите натуральное число: "))
    
    result = count(n)
    print(f"Количество цифр в числе {n} = {result}")


if __name__ == "__main__":
    main()
