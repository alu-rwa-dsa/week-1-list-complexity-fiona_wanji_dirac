import random
import memory_profiler
from memory_profiler import profile
import time
import timeit
import matplotlib.pyplot as plt

code_set = "import time"

@profile
def my_lower(str_1):
    new_str = ""
    lst_idx = []
    lst_time = []
    lst_space = []
    _index = 0
    for letter in str_1:
        seconds_1 = time.time()
        _index += 1
        lst_idx.append(_index)
        new_str += letter.lower()
        seconds_2 = time.time()
        time_t = seconds_2 - seconds_1
        space = memory_profiler.memory_usage()
        if len(lst_space) == 0:
            lst_space.append(space[-1])
        else:
            lst_space.append(space[-1] + lst_space[-1])
        if len(lst_time) == 0:  
            lst_time.append(time_t)
        else:
            lst_time.append(time_t + lst_time[-1])
    print(new_str)
    return lst_time, lst_space, lst_idx

lst_time, lst_space, lst = my_lower("I am So TIREDDDDDDDDDDDDDDDD")

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
        
