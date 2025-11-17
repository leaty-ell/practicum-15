def odd_list(a, n) -> list:
    """
    Recursive function to return list of even numbers.
    
    Args:
        a (list): List of integers
        n (int): Number of elements (optional)
        
    Returns:
        list: List containing only even numbers
    """
    if n is None:
        n = len(a)
    
    if n == 0:
        return []
    else:
        rest_even = odd_list(a[1:], n - 1)
        if a[0] % 2 == 0:
            return [a[0]] + rest_even
        else:
            return rest_even


def main():
    """
    Main function to get input from keyboard
    """
    numbers = list(map(int, input("Введите числа через пробел: ").split()))
    
    result = odd_list(numbers)
    print(f"Четные числа: {result}")


if __name__ == "__main__":
    main()

