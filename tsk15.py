def ten_to_bin(x) -> str:
    """
    Recursive function to convert decimal number to binary string.
    
    Args:
        x (int): Natural number in decimal
        
    Returns:
        str: Binary representation as string
    """
    if x == 0:
        return "0"
    elif x == 1:
        return "1"
    else:
        return ten_to_bin(x // 2) + str(x % 2)


def main():
    """
    Main function to get input from keyboard
    """
    x = int(input("Введите натуральное число: "))
    
    result = ten_to_bin(x)
    print(f"Двоичное представление: {result}")


if __name__ == "__main__":
    main()
