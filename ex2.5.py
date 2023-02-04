import json
import sys
import timeit
import matplotlib.pyplot as plt
import random

from numpy import median

with open("C:/Users/Evan/ex2.json", 'r') as file:
    content = json.load(file)

def get_mid(list):
    len_list = len(list)
    max_item = max(list)
    low_diff = abs((max_item // 2) - list[0])
    i = 0
    middle_most = 0
    for elem in list:
        if (abs(max_item // 2 ) - list[i]) < low_diff:
            low_diff = (abs(max_item // 2 ) - list[i])
            middle_most = i
        i += 1
    midvalitem = list[middle_most]
    return midvalitem

for object in content:
    random.shuffle(object)    # shuffle the items in the sub-array; this prevents/ minimizes ascending/descending order for the array/
    median = get_mid(object)  # fetch the median from each sub-array in parent array
    lenobj = len(object)        # length of sub - array
    med_ind = object.index(median) # gets the median index number
    temp = object[lenobj//2]
    object[lenobj//2] = median
    object[med_ind] = temp
   

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
