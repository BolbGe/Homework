n = int(input())
s = 0
l = 0

for i in range(n):
    wrd = input()
    counterA = 0
    ln = len(wrd)
    counterA = wrd.count("a")
    if counterA > ln - counterA:
        s += 1

if s > n//2:
    l = 1
print(s, l)