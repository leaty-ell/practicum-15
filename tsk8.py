def fib(k) -> int:
    """
    Recursive function to calculate k-th Fibonacci number.
    
    Args:
        k (int): Index in Fibonacci sequence
        
    Returns:
        int: k-th Fibonacci number
    """
    if k <= 1:
        return k
    else:
        return fib(k - 1) + fib(k - 2)


def main():
    """
    Main function to get input and display result
    """
    k = int(input("Введите номер члена последовательности Фибоначчи: "))
    
    result = fib(k)
    print(f"{k}-й член последовательности Фибоначчи = {result}")


if __name__ == "__main__":
    main()
