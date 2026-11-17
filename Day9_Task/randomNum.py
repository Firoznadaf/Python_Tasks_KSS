# Random Number Generator (Generators) 

def generate_number(n):
    for i in range(1, n + 1):
        yield i

n = 5

for num in generate_number(n):
    print(num)