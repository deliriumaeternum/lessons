def is_prime(func):
    def wrapper(*args):
        is_primes = True
        result_func = func(*args)
        for i in range(2, result_func):
            if result_func % i == 0:
                is_primes = False
        if is_primes:
            print("Простое")
        else:
            print("Составное")
        return result_func
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)