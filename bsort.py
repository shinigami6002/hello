def bubblesort(data):
    for i in range(len(data)):
        for j in range(0, len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]


data = [4, 3, 7, 2, 8]
bubblesort(data)
print(data)
