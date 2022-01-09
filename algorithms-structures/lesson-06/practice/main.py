

def foo(perem1):
    global perem
    perem += 1


perem = 1
foo(perem)

print(perem)