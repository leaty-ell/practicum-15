def search(a: list, x: int) -> int:
    """
    Recursive function to search for number x in list a.
    
    Args:
        a (list): List of integers
        x (int): Number to search for
        
    Returns:
        int: 1 if found, 0 if not found
    """
    if not a:
        return 0
    elif a[0] == x:
        return 1
    else:
        return search(a[1:], x)


def main():
    numbers = list(map(int, input("Введите числа через пробел: ").split()))
    x = int(input("Введите число для поиска: "))
    
    result = search(a, x)
    if result == 1:
      print(f"Число {x} найдено в списке")
    else:
      print(f"Число {x} не найдено в списке")


if __name__ == "__main__":
    main()
  
