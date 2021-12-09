# [3, 5, -4, 8, 11, 1, -1, 6], find 2 numbers sum to 10
import cProfile
import numpy as np
# keep the random the same everytime we run
np.random.seed(0)

sum_should_be = 10
array = [3, 5, -4, 8, 11, 1, -1, 6]
array = np.random.randint(-10, 10, 10000)


def solution_1():
    existed = []
    results = []
    for num in array:
        looking_num = sum_should_be - num
        if looking_num in existed:
            results.append((looking_num, num))
        elif num not in existed:
            existed.append(num)

    # print(results)


def solution_2():
    existed = {}
    results = []
    for num in array:
        looking_num = sum_should_be - num
        if looking_num in existed:
            results.append((looking_num, num))
        else:
            existed[num] = True

    # print(results)


cProfile.run("solution_2()")
