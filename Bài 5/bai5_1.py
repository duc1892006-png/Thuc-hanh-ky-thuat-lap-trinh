# File: mymath.py
def square(n):
    return n * n

def cube(n):
    return n * n * n

def average(values):
    nvals = len(values)
    sum_vals = 0.0
    for v in values:
        sum_vals += v
    return float(sum_vals) / nvals
