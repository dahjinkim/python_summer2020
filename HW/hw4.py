import datetime
import random
import matplotlib.pyplot as plt
import os

os.chdir('/Users/jinki/Documents/GitHub/python_summer2020/HW')

####### Two Sorting mechanisms
# 1) Bubble sort (revised from Day 8 lecture and https://realpython.com/sorting-algorithms-python/)
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        Finished = True # make a check condition that can terminate the loop
        for j in range(n - i - 1):
            # first loop (i = 0) will compare every element and its adjacent elements
            # second loop (i = 1) will compare elements except the last element of the list
            # which is supposed to have been sorted in the first loop.
            if numbers[j] > numbers[j + 1]: # if an element is greater than the element adjacent to the right,
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j] # swap the elements
                Finished = False # change the condition to continue the loop
        if Finished: # if there's nothing left to sort
            break
    return numbers
# Complexity of O(n^2)

# 2) Merge Sort
# (revised from https://realpython.com/sorting-algorithms-python/
# and https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm)
# splitting function
def merge(left, right):
    result = [] # create an empty list
    while len(left) != 0 and len(right) != 0: # as long as input lists have elements
        if left[0] < right[0]: # compare
            result.append(left[0]) # append to the result
            left.remove(left[0]) # remove from input list
        else:
            result.append(right[0]) # append
            right.remove(right[0]) # remove
    # the while loop will stop when one of the list becomes empty
    if len(left) == 0: # if the empty list is the left one,
        result = result + right # add right list to result
    else: # vice versa
        result = result + left
    return result

# sorting function
def merge_sort(numbers):
    if len(numbers) <= 1: # if the input list has one element
        return numbers # no need to sort, return the input

    # Find the center point and devide the list
    center = len(numbers) // 2

    # Using recursion, dividing the input in half
    # sorting and merging them into the final result
    return merge(left = merge_sort(numbers[:center]), right = merge_sort(numbers[center:]))
# Complexity of O(nlog_{2}n)

####### Tests
number_list = [5, 25, 9, 2, 7, 13, 87]
print(bubble_sort(number_list)) # 2, 5, 7, 9, 13, 25, 87
print(merge_sort(number_list)) # 2, 5, 7, 9, 13, 25, 87
# They both work! Yay


###### Simulation
# 100 random list generating function with size(N)
# between numbers 0 and 10000
def ran_list(size):
    randomList = []
    for i in range(0, 100):
        randomList.append(random.sample(range(0, 10000), size))
    return randomList

# Time calculating function for sorting algorithms
# We will simulate 100 times for each size
def sort_time(size):
    # create empty list for measuring time
    bubble_time = []
    merge_time = []
    # make 100 random lists of a set size to simulate with
    lists = ran_list(size)
    # make a for loop to simulate
    for list in range(0, 100):
        # measuring time for bubble sort
        # record start time
        start_time = datetime.datetime.now()
        # run bubble sort
        bubble_sort(lists[list])
        # record end time
        end_time = datetime.datetime.now()
        # measure time taken
        time_taken = end_time - start_time
        # append to bubble_time list
        bubble_time.append(time_taken.microseconds)

        # measuring time for bubble sort
        start_time = datetime.datetime.now()
        merge_sort(lists[list])
        end_time = datetime.datetime.now()
        time_taken = end_time - start_time
        merge_time.append(time_taken.microseconds)

    return [bubble_time, merge_time]



###### Plotting
# Plot: Compare average running time of bubble_sort() and merge_sort()
# x-axis: N = 1000
x = range(1, 1001)
# y-axis: average time for 100 simulation for each size (N)
# create empty lists for each sorting algorithm
bubble_average = []
merge_average = []
for i in x:
    times = sort_time(i)
    bubble_time_average = sum(times[0])/100
    merge_time_average = sum(times[1])/100
    bubble_average.append(bubble_time_average)
    merge_average.append(merge_time_average)

# plot
plt.plot(x, bubble_average, label = 'Bubble Sort: O(n^2)')
plt.plot(x, merge_average, label = 'Merge Sort: O(nlog_{2}n)')
# plot title
plt.title("How different algorithm complexities affect runtime")
# axis label
plt.ylabel("Average runtime in microseconds")
plt.xlabel("N (size)")
