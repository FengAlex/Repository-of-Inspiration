print('          _  ∞\n 1     2√2  --   (4k)!(1103 + 26390k)\n--- = ------ >   ----------------------\n π    9801  --             4   4k\n             k = 0      (k!) 396\n')

def factorial(n) :
    if n == 0 :
        return 1
    else :
        m = n
        for i in range(1, n) :
            m *= i
        return m

def func(n) :
    return (factorial(4 * n) * (1103 + 26390 * n)) / (factorial(n) ** 4 * 396 ** (4 * k))

num = int(input('calculate times (must be int)>'))

a = (2 * 2 ** (1 / 2)) / 9801

out = 0
for k in range(num) :
    out += func(k)

pi = 1 / (a * out)

print(f'\nπ ≈ {pi}\n')
input('Hit enter to leave')
