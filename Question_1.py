import timeit
# Question 1
# tracking time taken to run an algorithm, we'll use random code to measure the time
code_set = "import time"

random_code = """
for z in range(10):
    print("I am " + str(z) + " years old")
"""
time_taken = timeit.timeit(setup=code_set, stmt=random_code, number=10000)
print("Execution time is " + str(time_taken))
