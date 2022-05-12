import multiprocessing as mp
from primePy import primes
from functools import reduce

def divisors(n):
    divisors = list()
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)

    return divisors

def task_1(n):
    """
    Task 1 → Encuentre la suma de todos los números enteros positivos n
    que no excedan 100 000 000 tal que para cada divisor d de n, d + n / d es primo.
    """
    numbers = set()
    divs = divisors(n)
    lenDivs = len(divs)
    filtered = list(filter(lambda x: primes.check((x + n)/ x), divs))
    if lenDivs == len(filtered):
        numbers.add(n)
    return numbers


pool = mp.Pool(mp.cpu_count())

limit = 100000000
range = range(1, limit+1)
results = pool.map(task_1, range)

pool.close()

results = reduce(lambda x,y: x.union(y), results)
print(results)
print("Suma: ", sum(results))
