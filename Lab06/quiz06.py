import math
import time


def time_function(func):
    def wrapper(*args):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished the function {func.__name__!r} in {run_time:.4f} seconds")
        return run_time
    return wrapper


@time_function
def eratosthenes_ronald(upperbound):
    numbers_list = list(range(2, upperbound + 1))
    position = 0

    if upperbound > 2:
        while numbers_list[position] < math.sqrt(upperbound):
            numbers_list = delete_multiples_of(numbers_list, numbers_list[position])
            position += 1

    return numbers_list


def delete_multiples_of(numbers_list, number):
    numbers_to_delete = []

    for i in range(len(numbers_list)):
        # For each integer in the list that is divisible by prime but is not prime, add that integer to a list
        if numbers_list[i] % number == 0 and numbers_list[i] != number:
            numbers_to_delete.append(numbers_list[i])

    for i in range(len(numbers_to_delete)):
        numbers_list.remove(numbers_to_delete[i])
    return numbers_list


@time_function
def eratosthenes_ralph(upperbound):
    primes = []
    for i in range(2, upperbound + 1):
        primes.append(i)
    for i in primes:
        if i <= (math.sqrt(upperbound)):
            for j in range(i * 2, upperbound + 1, i):
                if j in primes:
                    primes.remove(j)
    return primes


@time_function
def eratosthenes_kyrill(upperbound):
    prime_numbers = []
    for i in range(0, upperbound + 1):
        prime_numbers.append(i)
    if 0 in prime_numbers:
        prime_numbers.remove(0)
    if 1 in prime_numbers:
        prime_numbers.remove(1)
    i = 2
    while i < math.ceil(math.sqrt(upperbound)):
        if i in prime_numbers:
            for counter in range(i * 2, upperbound + 1, i):
                if counter in prime_numbers:
                    prime_numbers.remove(counter)
        i += 1
    return prime_numbers


def main():
    upper_bound = 10000
    kyrill_runtime = eratosthenes_kyrill(upper_bound)
    ralph_runtime = eratosthenes_ralph(upper_bound)
    ronald_runtime = eratosthenes_ronald(upper_bound)
    fastest_runtime = [kyrill_runtime, ralph_runtime, ronald_runtime]
    fastest_runtime.sort()
    name = "Kyrill"
    if fastest_runtime[0] == ronald_runtime:
        name = "Ronald"
    elif fastest_runtime[0] == ralph_runtime:
        name = "Ralph"
    print(f"The fastest algorithm is {fastest_runtime[0]:.4f} seconds, which belongs to {name}")


if __name__ == "__main__":
    main()
