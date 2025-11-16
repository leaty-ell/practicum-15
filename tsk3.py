def progress(a1, r, n) -> float:
  """
    Recursive function to find the n-th term of an arithmetic progression.
    
    Args:
        a1 (float): First term of the progression
        r (float): Common difference
        n (int): Term number (natural number)
    
    Returns:
        float: The n-th term of the arithmetic progression
    """
    if n == 1:
        return a1
    else:
        return r + progress(a1, r, n - 1)


def main():
    """
    Main function to get input from keyboard
    """
    a1 = float(input("Введите первый член прогрессии a1: "))
    r = float(input("Введите разность прогрессии r: "))
    n = int(input("Введите номер члена n: "))
    
    result = progress(a1, r, n)
    print(f"{n}-й член прогрессии = {result}")


if __name__ == "__main__":
    main()
