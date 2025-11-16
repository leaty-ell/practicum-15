def mod_number(a, b) -> int:
    """
    Recursive function to find the remainder of division of natural number a by b.
    
    Args:
        a (int): Dividend (natural number)
        b (int): Divisor (natural number)
    
    Returns:
        int: Remainder of a divided by b
    """
    if a < b:
        return a
    else:
        return mod_number(a - b, b)


def main():
    """
    Main function to get input from keyboard
    """
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    
    result = mod_number(a, b)
    print(f"Остаток от деления {a} на {b} = {result}")


if __name__ == "__main__":
    main()
