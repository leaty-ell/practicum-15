def ind_maxlist(a: list, index: int = 0) -> int:
    """
    Recursive function to find the index of maximum element in list.
    
    Args:
        a (list): List of integers
        index (int): Current index (for recursion)
        
    Returns:
        int: Index of maximum element
    """
    if len(a) == 1:
        return index
    else:
        max_rest_index = ind_maxlist(a[1:], index + 1)
        return (
            index if a[0] > a[max_rest_index - index] 
            else max_rest_index
        )


def main():
    """
    Main function to get input from keyboard
    """
    numbers = list(map(int, input("Введите числа через пробел: ").split()))
    result = ind_maxlist(numbers)
    print(f"Индекс максимального элемента: {result}"


if __name__ == "__main__":
    main()
