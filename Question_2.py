import memory_profiler
from memory_profiler import profile
# Question 2
# tracking the space used by an algorithm


@profile(precision=4)
def func():
    a = int(60) * (10 / 809)
    print(a)


func()
space = memory_profiler.memory_usage()
print(space[-1])
