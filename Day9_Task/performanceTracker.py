# Performance Tracker (Decorators) 

import time

def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()

        print("Execution Time:", end - start, "seconds")

    return wrapper

@calculate_time
def display():
    for i in range(100000):
        pass
    print("Task Completed")

display()