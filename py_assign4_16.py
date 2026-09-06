class Fibonacci:

    def __init__(self, n):
        self.n = n

    # Recursive method
    def recursive(self, n):
        if n <= 1:
            return n

        return self.recursive(n - 1) + self.recursive(n - 2)

    # Dynamic Programming method
    def dynamic(self):
        if self.n <= 0:
            return 0

        if self.n == 1:
            return 1

        a = 0
        b = 1

        for i in range(2, self.n + 1):
            a, b = b, a + b

        return b

    # Display Fibonacci sequence
    def display_sequence(self):
        sequence = []

        a = 0
        b = 1

        for i in range(self.n + 1):
            sequence.append(a)
            a, b = b, a + b

        return sequence


# Main program
n = int(input("Enter the value of n: "))

fib = Fibonacci(n)

print("\nFibonacci Sequence:")
print(fib.display_sequence())

print("\nUsing Recursion:")
print("Fibonacci number at position", n, "=", fib.recursive(n))

print("\nUsing Dynamic Approach:")
print("Fibonacci number at position", n, "=", fib.dynamic())