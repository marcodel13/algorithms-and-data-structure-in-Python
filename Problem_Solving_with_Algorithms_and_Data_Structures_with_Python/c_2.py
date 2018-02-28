# a = [0,1,2,3,10,5,6,7,8,9]


# O(n2)
# for k in a:
#     for l in a:
#         print(k, l)

# O(n)
# max = 0
# max = sorted(a)[-1]
# print(max)


# Devise an experiment that compares the performance of the del operator on lists and dictionaries
'''
import time
import matplotlib.pyplot as plt

l_values = []

for i in range(10000,1000001,20000):
    l = list(range(i))
    d = {j:None for j in range(i)}

    t_start = time.time()



    # list_time = time.time()
    #
    del d[1000]
    dic_time = time.time()

    l_values.append((dic_time-t_start))

plt.plot(l_values)
plt.show()
'''

# Given a list of numbers in random order
# write a linear time algorithm to find the kth smallest number in the list.
# Explain why your algorithm is linear

import random

num_items = 20
rand_list = random.sample(range(num_items, num_items*2),num_items)


def select_random_pivot(array, k):
    '''
    Implementation of the random select algorithm as described in CLRS
    "Introduction to Algorithms, 3rd Edition" on page 216 modified to
    partition the items in separate lists.

    This algorithm has a worst case run time of O(N^2) where N is the
    number of entries in the array but the probability of that occuring
    is vanishingly small. The average case is O(N). It is normally much
    faster than select_median_of_medians_pivot.

    Here is how you might use it:

        # Create a list of pseudo random numbers.
        # Duplicates can occur.
        num = 10000
        array = [random.randint(1,1000) for i in range(num)]
        random.shuffle(array)
        random.shuffle(array)

        # Get the value of the kth item.
        k = 7
        kval = select_random_pivot(array, k)

        # Test it.
        sorted_array = sorted(array)
        assert sorted_array[k] == kval

    @param array the list of values
    @param k     k-th item to select.
    @returns the k-th item
    '''

    # If the array is short, terminate the recursion and return the
    # value without partitioning.
    if len(array) <= 10:
        array.sort()
        return array[k]

    # Randomly choose a pivot point.
    # In vanishingly rare cases this can result in O(N^2).
    pivot_idx = random.randint(0, len(array) - 1)
    pivot = array[pivot_idx]  # pivot point value (not index)

    # Now select recursively using the pivot.
    # At this point we have the pivot. Use it to partition the input
    # array into 3 categories: items that are less than the pivot
    # value (array_lt), items that are greater than the pivot value
    # (array_gt) and items that exactly equal to the pivot value
    # (equals_array).
    array_lt = []
    array_gt = []
    array_eq = []
    for item in array:
        if item < pivot:
            array_lt.append(item)
        elif item > pivot:
            array_gt.append(item)
        else:
            array_eq.append(item)

    # The array values have been partitioned according to their
    # relation to the pivot value. The partitions look like this:
    #
    #   +---+---+---+...+---+---+---+...+---+---+---+...
    #   | 0 | 1 | 2 |   | e |e+1|e+2|   | g |g+1|g+2|
    #   +---+---+---+...+---+---+---+...+---+---+---+...
    #      array_lt        array_eq       array_gt
    #
    # If the value of k is in the range [0..e) then we know that
    # the desired value is in array_lt so we need to recurse.
    #
    # If the value of k in the range [e..g) then we know that the
    # desired value is in array_eq and we are done.
    #
    # If the value of k is >= g then we the desired value is in
    # array_gt and we need to recurse but we also have to make sure
    # that k is normalized with respect to array_gt so that it has the
    # proper offset in the recursion. We normalize it by subtracting
    # len(array_lt) and len(array_eq).
    #
    if k < len(array_lt):
        return select_random_pivot(array_lt, k)
    elif k < len(array_lt) + len(array_eq):
        return array_eq[0]
    else:
        normalized_k = k - (len(array_lt) + len(array_eq))
        return select_random_pivot(array_gt, normalized_k)

print(select_random_pivot(rand_list, 2))

def marco(array, k):

    pivot_idx = random.randint(0, len(array) - 1)
    pivot = array[pivot_idx]  # pivot point value (not index)

    array_lt = []
    array_gt = []

    for item in array:
        if item < pivot:
            array_lt.append(item)
        elif item > pivot:
            array_gt.append(item)

    if k < len(array_lt):
        return marco(array_lt, k)

print(marco(rand_list, 2))