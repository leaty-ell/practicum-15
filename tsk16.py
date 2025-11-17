def ten_to_n(x, n) -> str:
    """
    Recursive function to convert number from decimal to base-n system.
    
    Args:
        x (int): Natural number in decimal system
        n (int): Base of numeral system (2 ≤ n ≤ 16)
        
    Returns:
        str: Number in base-n system as string
    """
    digits = "0123456789ABCDEF"
    
    if x < n:
        return digits[x]
    else:
        return ten_to_n(x // n, n) + digits[x % n]


def main(): 
  """
  Main function to get input from keyboard
  """
  x = int(input("Введите натуральное число: "))
  n = int(input("Введите основание системы (2-16): "))
        
  result = ten_to_n(x, n)
  print(f"Число {x} в {n}-ричной системе: {result}")


if __name__ == "__main__":
    main()
