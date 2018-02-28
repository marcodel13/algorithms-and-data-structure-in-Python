# ******************
#  Sequential Search
# ******************

'''
start from the beginning and go through all the items in the list
remember: with both ordered and unordered lists, you have O(n).
the only difference is on the worst case, which is n for unordered and n1/2 for order is
the item is not present
'''

def sequential_search(a_list, item):

    found = False

    for element in a_list:
        if element == item:
            found = True
            return found

    return found


# test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(sequential_search(test_list, 3))
# print(sequential_search(test_list, 13))


def ordered_sequential_search(a_list, item):

    found = False

    for element in a_list:
        print('looking at element', element)
        if element > item:
            return found
        else:
            if element == item:
                found = True
                return found
    return found


# print(ordered_sequential_search(sorted(test_list), 43))

# ******************
#    Binary Search
# ******************

'''
you need an ordered list to use this.
start from the middel of the list. If the item we are searching for is greater than the middle item,
we know that the entire lower half of the list as well as the middle item can be eliminated from further consideration.
The item, if it is in the list, must be in the upper half
'''

# version by marco
def binary_search_marco(a_list, item):

    found = False

    len_list = len(a_list)

    iterations = 0

    while len_list > 0 and found == False: # note: you have to keep track not only of the found/no found, but also
                                           # of the length of the list: when it comes to be equal to 0, you have to stop

        iterations += 1
        print("iteration:", iterations)

        print('middel point',a_list[int(len_list/2-1)])

        if item > a_list[int(len_list/2-1)]:
            print('item={0} larger than middle point={1}'.format(item, a_list[int(len_list / 2-1)]))
            a_list = a_list[int(len_list / 2):]
            len_list = len(a_list)

        elif item < a_list[int(len_list/2-1)]:
            print('item={0} smaller than middle point={1}'.format(item, a_list[int(len_list / 2-1)]))
            a_list = a_list[:int(len_list/2)]
            len_list = len(a_list)

        elif item == a_list[int(len_list/2-1)]:
            print('item found', item)
            found = True
            return found



    return found

# l = [1,2,3,4,5,6,7,8]



def binary_search(a_list, item):

    first = 0
    last = len(a_list) - 1
    found = False

    iterations = 0
    while first <= last and not found:
        iterations += 1
        print("iterations", iterations)


        print(first, last)
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# print(binary_search(test_list, 3))
# print(binary_search(test_list, 13))
print(binary_search_marco(test_list, 13))