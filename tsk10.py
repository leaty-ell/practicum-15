def maxlist(a) -> int:
    """
    Recursive function to find maximum element in list.
    
    Args:
        a (list): List of integers
        
    Returns:
        int: Maximum element in the list
    """
    if len(a) == 1:
        return a[0]
    else:
        max_rest = maxlist(a[1:])
        return a[0] if a[0] > max_rest else max_rest


def main():
    """
    Main function to get input and display result
    """
    numbers = list(map(int, input("Введите числа через пробел: ").split()))
    
    if numbers:
        result = maxlist(numbers)
        print(f"Максимальный элемент в списке: {result}")
    else:
        print("Список пуст")


if __name__ == "__main__":
    main()
