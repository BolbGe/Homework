from itertools import product

c = 0

alp = '0123456789'

def mask(n, alp):
    c = 0
    for i in range(10):
        el = str(i)
        for j in product(alp, repeat=n):
            st = ''
            for k in j:
                st = st + str(k)
            num = f'1{el}80{st}'
            num = int(num)
            subcounter = 0
            for i in range(1, int(num**1/2)+2):
                if num % i == 0:
                    subcounter += 1
            if subcounter % 2 != 0:
                c += 1
    return c

for i in range(4):
    c += mask(i, alp)

print(c)