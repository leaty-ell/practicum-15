def simmetr(s: str, i: int, j: int) -> bool:
    """
    Recursive function to check if substring s[i:j+1] is symmetric (palindrome).
    
    Args:
        s (str): Input string
        i (int): Start index of substring
        j (int): End index of substring
        
    Returns:
        bool: True if substring is symmetric, False otherwise
    """
    if i >= j:
        return True
    
    if s[i] != s[j]:
        return False
      
    return simmetr(s, i + 1, j - 1)


def main():
    """
    Main function to get input from keyboard
    """
    s = input("Введите строку: ")
    i = int(input("Введите начальный индекс: "))
    j = int(input("Введите конечный индекс: "))
    
    result = simmetr(s, i, j)
    substring = s[i:j+1]
    if result:
        print(f"Подстрока '{substring}' является симметричной")
    else:
        print(f"Подстрока '{substring}' не является симметричной")


if __name__ == "__main__":
    main()
