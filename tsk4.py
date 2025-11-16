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


def sum_progress(a1, r, n) -> float:
    """
    Recursive function to find the sum of first n terms of arithmetic progression.
    
    Args:
        a1 (float): First term of the progression
        r (float): Common difference
        n (int): Number of terms to sum
    
    Returns:
        float: Sum of first n terms of the progression
    """
    if n == 1:
        return a1
    else:
        return progress(a1, r, n) + sum_progress(a1, r, n - 1)


def main():
    a1 = float(input("Введите первый член прогрессии a1: "))
    r = float(input("Введите разность прогрессии r: "))
    n = int(input("Введите количество членов n: "))
    
    result = sum_progress(a1, r, n)
    print(f"Сумма первых {n} членов прогрессии = {result}")


if __name__ == "__main__":
    main()
