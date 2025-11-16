def nod(a, b) -> int:
    """
    Recursive function to calculate GCD of two natural numbers.
    
    Args:
        a (int): First natural number
        b (int): Second natural number
        
    Returns:
        int: Greatest common divisor of a and b
    """
    if b == 0:
        return a
    else:
        return nod(b, a % b)


def main():
    """
    Main function to get input and display result
    """
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    
    result = nod(a, b)
    print(f"НОД чисел {a} и {b} = {result}")


if __name__ == "__main__":
    main()
