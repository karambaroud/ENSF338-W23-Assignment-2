import timeit
import matplotlib.pyplot as plt

#Original function
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

#Improved function
cache = {}
def func2(n):
    if n == 0 or n == 1:
        return n
    elif n in cache.keys():
        return cache[n]
    else:
        cache[n] = func2(n-1) + func2(n-2)
        return cache[n]

#Empirical analysis of the original function.
func_time_list = []
for i in range(0, 36):
    elapsed_time = timeit.timeit(lambda : func(i), number=1)
    func_time_list.append(elapsed_time)

#Empirical analysis of the improved function.
func2_time_list = []
for i in range(0, 36):
    elapsed_time = timeit.timeit(lambda : func2(i), number=1)
    func2_time_list.append(elapsed_time)

#Plotting the results
fig, axs = plt.subplots(figsize = (10, 5))

axs1 = plt.subplot2grid ( shape = (1,2), loc = (0,0))
axs2 = plt.subplot2grid ( shape = (1,2), loc = (0,1))
plt.tight_layout()

axs1.plot(func_time_list, label='original')
axs1.legend(loc='upper left')
axs1.set_xlabel('Argument')
axs1.set_ylabel('Time (s)')

axs2.plot(func2_time_list, color="r", label='improved')
axs2.legend(loc='upper left')
axs2.set_xlabel('Argument')
axs2.set_ylabel('Time (s)')

plt.show()

