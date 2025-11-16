def degree5(n: int) -> int:
       """
    Recursive function to check if n is a power of 5.
    
    Args:
        n (int): Natural number to check
        
    Returns:
        int: Exponent if n is power of 5, -1 otherwise
    """
    if n == 1:
        return 0
    elif n % 5 != 0 or n < 1:
        return -1
    else:
        result = degree5(n // 5)
        return result + 1 if result != -1 else -1


def main():
  """
  Main function to get input and display result
  """
    n = int(input("Введите натуральное число: "))
    
    result = degree5(n)
    if result == -1:
        print(f"Число {n} не является степенью числа 5")
    else:
        print(f"Число {n} = 5 в степени {result}")


if __name__ == "__main__":
    main()
