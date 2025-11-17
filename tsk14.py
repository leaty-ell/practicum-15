def numbers(x: int):
    """
    Recursive function to print digits of natural number in reverse order.
    
    Args:
        x (int): Natural number
    """
    if x < 10:
        print(x)
    else:
        print(x % 10)
        numbers(x // 10)


def main():
    """
    Main function to get input from keyboard
    """
    x = int(input("Введите натуральное число: "))
    
    print("Цифры в обратном порядке:")
    numbers(x)


if __name__ == "__main__":
    main()
