#  Infinite Even Number Generator (Generators)

def even_numbers():
    n = 2
    while True:
        yield n 
        n += 2

N = 5
gen = even_numbers()

for i in range(N):
    print(next(gen))