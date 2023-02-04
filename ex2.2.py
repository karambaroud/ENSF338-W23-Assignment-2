import json
import sys
import timeit
import matplotlib.pyplot as plt
 
with open("ex2.json", "r") as file:
    content = json.load(file)

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def itemin():
    times = []
    for numlist in content:
        elapsed_time = timeit.timeit(lambda : func1(numlist, 0, len(numlist)-1), number=1)
        times.append(elapsed_time)
    
    plt.bar(range(len(times)), times)
    plt.xlabel("Lists")
    plt.ylabel("Time (s)")
    plt.show()

if __name__ == '__main__':
    itemin()
