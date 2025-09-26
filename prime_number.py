import sys

print("This is a prime number module.")

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def ith_prime(i):
    count = 0
    num = 1
    while count < i:
        num += 1
        if is_prime(num):
            count += 1
    return num

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 prime_number.py <i>")
        sys.exit(1)
    try:
        i = int(sys.argv[1])
        if i < 1:
            raise ValueError
    except ValueError:
        print("Please provide a positive integer for i.")
        sys.exit(1)
    print(f"The {i}-th prime number is: {ith_prime(i)}")
