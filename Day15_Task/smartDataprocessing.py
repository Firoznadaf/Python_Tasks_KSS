

import os
import numpy as np
import pandas as pd
import time

# file path
script_folder = os.path.dirname(os.path.abspath(__file__))
numbers_file = os.path.join(script_folder, "numbers.txt")

# Create sample file
with open(numbers_file, "w") as file:
    file.write("10\n20\n30\n40\n50\nabc\n60\n")


# Decorator to calculate execution time
def calculate_time(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution Time:", end - start)

        return result

    return wrapper


# Generator to read numbers
def read_numbers(filename):

    with open(filename, "r") as file:

        for line in file:

            try:
                yield float(line.strip())

            except ValueError:
                print("Invalid data:", line.strip())


@calculate_time
def process_data():

    numbers = list(read_numbers("numbers.txt"))

    if len(numbers) == 0:
        print("No valid numbers found")
        return

    # NumPy calculations
    mean = np.mean(numbers)
    std = np.std(numbers)

    print("Numbers:", numbers)
    print("Mean:", mean)
    print("Standard Deviation:", std)

    # Convert into DataFrame
    df = pd.DataFrame({
        "Mean": [mean],
        "Standard Deviation": [std]
    })

    print("\nDataFrame:")
    print(df)


try:
    process_data()

except IOError:
    print("Unable to read file")