# [2,3,4,8,7,6]
# (n) + (n-1) + (n-2) + (n-3) + (n-n)
# (5) + (4) + (3) + (2) + (1) + 0 aka summation

def selection_sort(data: list):
    n = len(data)

    for i in range(n):
        minIndex = i

        for j in range(i, n):
            if data[j] < data[minIndex]:
                minIndex = j
        
        # swap current index with min val
        if i != minIndex:
            temp = data[minIndex]
            data[minIndex] = data[i]
            data[i] = temp

    return data


print(selection_sort([2, 3, 4, 8, 7, 6]))
