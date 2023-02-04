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

#Duplicate the quicksort functions func1 and func2 to work with a pivot that is the median of the first, middle, and last elements of the array
def func3(arr, low, high):
    if low < high:
        pi = func4(arr, low, high)
        func3(arr, low, pi-1)
        func3(arr, pi + 1, high)

def func4(array, start, end):
    p = median(array, start, end)
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

def median(array, start, end):
    mid = (start + end) // 2
    if array[start] > array[mid]:
        array[start], array[mid] = array[mid], array[start]
    if array[start] > array[end]:
        array[start], array[end] = array[end], array[start]
    if array[mid] > array[end]:
        array[mid], array[end] = array[end], array[mid]
    array[mid], array[start] = array[start], array[mid]
    return array[start]


def itemin():
    times_func1 = []
    times_quicksort2 = []
    for numlist in content:
        elapsed_time_func1 = timeit.timeit(lambda : func1(numlist, 0, len(numlist)-1), number=1)
        times_func1.append(elapsed_time_func1)
        elapsed_time_quicksort2 = timeit.timeit(lambda : func3(numlist, 0, len(numlist)-1), number=1)
        times_quicksort2.append(elapsed_time_quicksort2)
    
    # Plot both lists on two different bar charts

    fig, axs = plt.subplots(figsize = (10, 5))

    axs1 = plt.subplot2grid ( shape = (1,2), loc = (0,0))
    axs2 = plt.subplot2grid ( shape = (1,2), loc = (0,1))
    plt.tight_layout()

    axs1.bar(range(len(times_func1)), times_func1)
    axs1.set_xlabel("Lists")
    axs1.set_ylabel("Time (s)")
    axs1.set_title("Original Quicksort")

    axs2.bar(range(len(times_quicksort2)), times_quicksort2)
    axs2.set_xlabel("Lists")
    axs2.set_ylabel("Time (s)")
    axs2.set_title("Improved Quicksort")

    plt.show()

if __name__ == '__main__':
    itemin()
