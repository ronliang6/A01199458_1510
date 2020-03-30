import doctest
import time
import statistics


def time_function(func):
    """
    Return a function that returns and logs the time a given function takes to run.

    Given a function as a parameter func, this function will return a wrapper function that records information about
    how long the parameter function took to run. The code in the parameter func will be run but the return value will
    not be used. The wrapper function will return the time taken for the code to run as a float.

    :param func: a function with no keyword arguments.
    :precondition: provide the function with an argument as defined by the PARAM statement above.
    :postcondition: return a function that invokes the function provided as func and record, log, and return the
    time it took to run.
    :return: a function.
    """
    def wrapper(*args):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished the function {func.__name__!r} in {run_time:.10f} seconds")
        with open('results.txt', 'a') as result_log:
            result_log.write(f"{func.__name__!r} with {args} as the argument(s) took {run_time:.10f} seconds\n")
        return run_time
    return wrapper


@time_function
def factorial_iterative(integer):
    """
    Calculate, log, and return the time it takes for a factorial to be calculated.

    :param integer: an integer larger or equal to zero.
    :precondition: provide the function with an argument as defined by the PARAM statement above.
    :postcondition: return an object as defined by the return statement below.
    :return: a float representing the length of time it took for the given function func to run.
    """
    factorial = 1
    while integer > 1:
        factorial *= integer
        integer -= 1
    return factorial


def factorial_recursive_helper(integer):
    """
    Calculate and return the factorial of an integer.

    :param integer: an integer greater or equal to zero.
    :precondition: provide the function with an argument as defined by the PARAM statement above.
    :postcondition: return an object as defined by the return statement below.
    :return: an integer representing the factorial of the given argument.

    >>> factorial_recursive_helper(0)
    1
    >>> factorial_recursive_helper(1)
    1
    >>> factorial_recursive_helper(2)
    2
    >>> factorial_recursive_helper(5)
    120
    >>> factorial_recursive_helper(10)
    3628800
    >>> factorial_recursive_helper(50)
    30414093201713378043612608166064768844377641568960512000000000000
    """
    return factorial_recursive_helper(integer - 1) * integer if integer > 1 else 1


@time_function
def factorial_recursive(integer):
    """
    Calculate, log, and return the time it takes for a factorial to be calculated.

    :param integer: an integer larger or equal to zero.
    :precondition: provide the function with an argument as defined by the PARAM statement above.
    :postcondition: return an object as defined by the return statement below.
    :return: a float representing the length of time it took for the given function func to run.
    """
    return factorial_recursive_helper(integer)


def main():
    """
    Clear all text in a file and then log runtime information for two functions.

    Will find the run-time ratios of the iterative factorial function and the recursive factorial function for
    factorials in the range [1, 100], and then print out the mean ratio.
    """
    doctest.testmod()
    with open('results.txt', 'w') as result_log:
        result_log.truncate(0)
    function_run_time_ratios = []
    for i in range(1, 101):
        iterative_run_time = factorial_iterative(i)
        recursive_run_time = factorial_recursive(i)
        ratio = iterative_run_time/recursive_run_time
        function_run_time_ratios.append(ratio)
    average_ratio = statistics.mean(function_run_time_ratios)
    print(f"On average, the iterative function is takes {average_ratio*100:.2f}% as much time to run compared to the "
          f"recursive function.")


if __name__ == "__main__":
    main()
