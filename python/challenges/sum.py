def sum(x, y):
    return x + y

def sumtimes(x, y, times):
    return sum(x, y) * times

def sum_times(x, y, times):
    if times == 0:
        return 0
    else:
        return sum(x, y) + sum_times(x, y, times - 1)

def summation(i, n):
    if n == 0:
        return 0
    else:
        return i + summation(i + 1, n - 1)