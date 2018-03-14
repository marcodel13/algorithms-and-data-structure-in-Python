# ******************
#  Bubble Sort
# ******************

'''
given a list of n items, start from the left, compare the first to the second: if the 1^ is bigger, swap them. Then the same for 2^ and 3^, etc.
If you have n items, there are n-1 possible comparisons.
You need to repeat the process n-1 times (i.e. you have n-1 passes)
Complexity is O=n2.
A bubble sort is often considered the most inefficient sorting method since it must exchange items before the final location is known.
These “wasted” exchange operations are very costly.
It has one advantage compared to the others, i.e. that if no exchanges are made, we now that the list is already sorted, and we can stop it.
'''


def bubble_sort_marco(a_list):

    n = len(a_list)


    # define the number of passes
    for i in range(n-1):
        changes_made = 0 # keep the count, cause if this is equal to zero, you can stop the algorithm

        print('pass {0}'.format(i))

        # perform a pass
        k = 0

        while k < n-1:

            # note: the chunck below is fine, cause it uses a temp assignment, but Python allows simultaneous assignment (see below)
            '''
            item_1 = a_list[k]
            item_2 = a_list[k+1]

            if item_1 > item_2:

                a_list[k] = item_2
                a_list[k+1] = item_1
            '''

            # simultaneous assignment
            if a_list[k] > a_list[k+1]:
                a_list[k], a_list[k+1] = a_list[k+1], a_list[k]

                changes_made +=1

            k+=1

        print('current list', a_list)

        if changes_made == 0:
            print('no changes made, stop the algorithm')
            break

    print('final list', a_list)

    return a_list

# l = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# l = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
# bubble_sort_marco(l)


# ******************
#  Selection Sort
# ******************

'''
It makes only one exchange for every pass through the list: it looks for the largest value as it makes a pass and, after completing the pass, places it in the proper location.
As with a bubble sort, after the first pass, the largest item is in the correct place.
Basically: at every pass you pick the highest value and bring it to the rigth, till the correct location.
It requires n - 1 passes to sort n items.
IMP:Selection sort makes the same number of comparisons as the bubble sort and is therefore also O(n2).
However, due to the reduction in the number of exchanges, the selection sort typically executes faster in benchmark studies
'''

a_list = [4,2,1,10,5,3,100]

def selection_sort_marco(a_list):

    n = len(a_list) - 1
    last_position = n

    for p in range(n):

        # perform a single pass
        k = 0
        temp = 0

        while k < last_position:

            current = a_list[k]
            if current > temp:

                temp = current
                pos = a_list.index(current)

            k += 1

        if temp > a_list[last_position]:

            a_list[last_position], a_list[pos] = temp, a_list[last_position]

        last_position -= 1

        p += 1


selection_sort_marco(a_list)

def selection_sort_book(a_list):
  for fill_slot in range(len(a_list) - 1, 0, -1):
     print(fill_slot)
     pos_of_max = 0
     for location in range(1, fill_slot + 1):
        if a_list[location] > a_list[pos_of_max]:
           pos_of_max = location
     temp = a_list[fill_slot]
     a_list[fill_slot] = a_list[pos_of_max]
     a_list[pos_of_max] = temp

selection_sort_book(a_list)
