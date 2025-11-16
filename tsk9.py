def combin(n, k) -> int:
    """
    Recursive function to calculate binomial coefficient C(n, k).
    
    Args:
        n (int): Total number of elements
        k (int): Number of elements to choose
        
    Returns:
        int: Number of combinations C(n, k)
    """
    if k == 0 or k == n:
        return 1
    else:
        return combin(n - 1, k - 1) + combin(n - 1, k)


def main():
    """
    Main function to get input and display result
    """
    n = int(input("Введите n: "))
    k = int(input("Введите k: "))
    
    result = combin(n, k)
    print(f"C({n}, {k}) = {result}")


if __name__ == "__main__":
    main()
