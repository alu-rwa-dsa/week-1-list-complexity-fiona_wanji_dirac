import random
import memory_profiler
from memory_profiler import profile
import time
import timeit
import matplotlib.pyplot as plt

code_set = "import time"

@profile
def sort_list():
    lst = []
    lst_time = []
    lst_space = []
    for i in range(1, 101):
        lst.append(i)
        time_t = timeit.timeit(setup = code_set, stmt=lst.sort, number= 1)
        space = memory_profiler.memory_usage()
        if len(lst_space) == 0:
            lst_space.append(space[-1])
        else:
            lst_space.append(space[-1] + lst_space[-1])
        if len(lst_time) == 0:  
            lst_time.append(time_t)
        else:
            lst_time.append(time_t + lst_time[-1])
    return lst_time, lst_space, lst

lst_time, lst_space, lst = sort_list()

plt.plot(lst, lst_space)
plt.xlabel('List Length')
plt.ylabel('Space')
plt.title("Space Complexity Graph")
plt.show()

plt.plot(lst, lst_time)
plt.xlabel('List Length')
plt.ylabel('Time')
plt.title("Time Complexity Graph")
plt.show()
