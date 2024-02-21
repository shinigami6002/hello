import time
start = time.perf_counter()


def lsearch(array, key):
    i = 0
    while i <= len(array):
        if array[i] == key:
            return i
        i += 1
    return -1


array = [4, 3, 6, 4]
key = 6
pos = lsearch(array, key)
if pos == -1:
    print("not found")
else:
    print("found at", pos)
end = time.perf_counter()
print("time taken", end-start)
