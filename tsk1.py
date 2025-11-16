def pownum(a, n) -> float:
      """
    Recursive function to calculate the power of a real number a raised to n.
    
    Args:
        a (float): Base number
        n (int): Exponent (natural number)
    
    Returns:
        float: Result of a raised to the power of n
    """
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        return a * pownum(a, n - 1)

def main():
    """Main function to get input from keyboard"""
    a = float(input("Введите число a: "))
    n = int(input("Введите степень n: "))
    
    result = pownum(a, n)
    print(f"{a} в степени {n} = {result}")


if __name__ == "__main__":
    main()
