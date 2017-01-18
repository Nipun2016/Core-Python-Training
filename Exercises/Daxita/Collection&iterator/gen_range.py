def gen_range(n):
    i = 0
    while i < n:
        yield i
        i += 1
n=int(input("Enter no: "))
g=gen_range(n)
print(next(g))
print(next(g))
