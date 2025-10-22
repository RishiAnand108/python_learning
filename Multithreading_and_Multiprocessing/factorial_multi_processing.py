import  multiprocessing
import math
import time
import sys

# increase the maxium nuber of digit for integer conversion
sys.set_int_max_str_digits(1000000)

## function to compute factorials of a given number

def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}") 
    return result

if __name__ == "__main__":
    numbers = [5000, 6000, 7000, 8000, 9000]

    start_time = time.time()

    # Create a pool of worker processes

    with multiprocessing.Pool(processes=5) as pool:
        # Map the function to the list of numbers
        results = pool.map(computer_factorial, numbers)
        end_time = time.time()

        print(f"Results: {results}")
        print(f"Time taken: {end_time - start_time} seconds")
