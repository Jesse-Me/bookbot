def sequence(a, b, c): 
    if a < b < c: 
        return a + b + c 

    if a >= b: 
        print(f"Recursing with: a={a-1}, b={b}, c={c}")
        return sequence(a - 1, b, c) 
    if a >= c: 
        print(f"Recursing with: a={c}, b={b}, c={a}")
        return sequence(c, b, a) 
    if b >= c: 
        print(f"Recursing with: a={c}, b={b}, c={a+2}")
        return sequence(c, b, a + 2) 
    return 0 

print(sequence(10, 10, 10))