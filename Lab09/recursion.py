import time


def time_function(func):
    def wrapper(*args):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished the function {func.__name__!r} in {run_time:.10f} seconds")
        with open('results.txt', 'a') as result_log:
            result_log.write(f"{func.__name__!r} took {run_time:.10f} seconds")
        return run_time

    return wrapper


@time_function
def factorial_iterative(integer):
    factorial = 1
    while integer > 1:
        factorial *= integer
        integer -= 1
    return factorial


def factorial_recursive_helper(integer):
    return factorial_recursive_helper(integer - 1) * integer if integer > 1 else 1


@time_function
def factorial_recursive(integer):
    return factorial_recursive_helper(integer)


def main():
    with open('results.txt', 'w') as result_log:
        result_log.truncate(0)
    print(factorial_iterative(10))
    print(factorial_recursive(10))


if __name__ == "__main__":
    main()
