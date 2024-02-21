def sel(data):
    n = len(data)
    for i in range(n):
        minpos = i
        for j in range(i+1, n):
            if data[j] < data[minpos]:
                minpos = j
        data[i], data[minpos] = data[minpos], data[i]


data = [24, 7, 2, 8]
sel(data)
print(data)
