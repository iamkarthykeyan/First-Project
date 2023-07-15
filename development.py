#Development codes

# A simple function to calculate the factorial of a number
def fibanacci(n):
    if n == 0:
        return 1
    else:
        return n * fibonacci(n - 1)

# A function to calculate the Fibonacci sequence
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# A function to print the Fibonacci sequence up to a given number
def print_fibonacci(n):
    for i in range(n):
        print(fibonacci(i))

if __name__ == "__main__":
    print_fibonacci(10)



