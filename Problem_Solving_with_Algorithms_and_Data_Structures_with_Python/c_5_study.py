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
The item, if it is in the list, must be in the upper half.
Remember that in this case O(log n)
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
# print(binary_search_marco(test_list, 13))


# ******************
#      Hashing
# ******************
'''
A hash table is a again a collection of items.
the hash table is simply a list, with each slot named with a value (0,1,2...n). Initially, slots contain no items (None), i.e. they are empty.
The mapping between an item and the slot where that item belongs in the hash table is called the hash function.
The hash function will take any item in the collection and return an integer in the range of slot names, between 0 and n-1.
The point is understanding what this has function does.
Suppose you have a hash table with 11 slots, from 0 to 10.
Suppose the items you want to insert in the table are the integers: 54,26,93,17,77, and 31.
You can use a has function usually called "remainder method", that basically takes an item and divides it by the table size,
using the remainder (il resto) as its hash value.
So, 54 % 11 = 10 --> 10 is the hash value, and 10 is the slot that will contain the item 54
26 % 11 = 4 --> 4 is the hash value, and 4 is the slot that will contain the item 26.

So, your list will end up being like this:

| 0 || 1 || 2 || 3 || 4 || 5 || 6 || 7 || 8 || 9 || 10|
-------------------------------------------------------
| 77||non||non||non|| 26|| 93|| 17||non||non|| 31|| 54|


The great thing is that when you have to look for a value, you compute its hash value and go directly to the slot which is supposed to
contain it. If the value is there, ok; otherwise, it means it is not in the list. Note that this makes O(1)!

Note: there can be collisions, if the hash function maps two items to the same slot - for example, if the list above included also 44, this item
would be mapped to slot 0, which is already occupied by 77 (because both 77%11 and 44%11 = 0).

Summing up: given a collection of items, a hash function that maps each item into a unique slot is referred to as a perfect hash function.
This is possibily given that all the items in a collection will never change.

Perfection can be achieved by using enormous amounts of memory, but this is impractical.

More concretely, the goal is to create a hash function that minimizes the number of collisions, is easy to compute,
and evenly distributes the items in the hash table.

There are a number of common ways to extend the simple remainder method: the folder method, the mid-square method

Collision is the main issue with hashing: it happens when two items hash to the same slot (e.g. 44 and 77 above).
Possible solutions are:
- linear probing: if an item hashes to a slot that is already taken, you move sequentially to the next slot, and so on, until you find one that is free.
  of course, when you then have to search for smt, you have to follow the same approach:if you hasha an item and it is not in the slot, you cannot
  just return False, but you have to search until either you find the item or we find an empty slot.
  problem: clustering --> item tend to cluster in a part of the list.
  solution: skip --> instead of moving slot by slot, you move three slots at a time. Note: the size of the skip has to ensure that you visit
  all the slots. To ensure this, it is often suggested that the table size be a prime number.
  The general name for this process of looking for another slot after a collision is rehashing.
  Alteernative solution: quadratic probing. Instead of using a constant “skip” value, you use a rehash function
  that increments the hash value by 1, 3, 5, 7, 9, and so on
- chaining: allow each slot to hold a reference to a collection (or chain) of items
  When you want to search for an item, you use the hash function to generate the slot where it should reside.
  Since each slot holds a collection, you use a searching technique to decide whether the item is present.


'''

def create_hash_table_marco(items_list, hash_table_length):

    hash_table = [None for x in range(hash_table_length)]

    for item in items_list:
        print(item)
        hash_value = item % hash_table_length
        print(hash_value)
        hash_table[hash_value] = item

    return hash_table

test_list = [54,26,93,17,77,31]
# create_hash_table_marco(test_list , 11)


# implementing the hash table as follows:
# Below we use two lists to create a HashTable class that implements the Map abstract data type.
# One list, called slots, will hold the key items and a parallel list, called data, will hold the data values.
# When we look up a key, the corresponding position in the data list will hold the associated data value.


# note, this implementation follows the description in the book, whereby the slots are defined as increasing numbers from 0 to len size
# below I implement a different version.
class HashTable:

    def __init__(self):
        self.size = 11
        # self.slots = [None for x in range(self.size)]
        self.data = [None for x in range(self.size)]

    def show(self):
        # print('slots:', self.slots)
        print('data:', self.data)

    def hash_function(self, item):
        print('item:', item)
        slot = item % self.size
        return slot

    def rehash(self, slot, item):
        while self.data[slot] != None:
            print('slot already taken at position', slot)
            if slot < self.size - 1:  # if you get to the end of the list, restart from position zero
                slot += 1
            else:
                slot = 0
        print('free slot found at positon', slot)
        self.data[slot] = item


    def put(self, item):
        print('item:', item)
        slot = self.hash_function(item)
        print('slot:', slot)

        if self.data[slot] == None:
            self.data[slot] = item
        else: # linear probing with a “plus 1” rehash function

            self.rehash(slot, item)
            # while self.data[slot] != None:
            #     print('slot already taken at position', slot)
            #     if slot < self.size-1: # if you get to the end of the list, restart from position zero
            #         slot += 1
            #     else:
            #         slot = 0
            # print('free slot found at positon',slot)
            # self.data[slot] = item

hashtable = HashTable()

hashtable.show()
hashtable.put(11)
hashtable.show()
hashtable.put(100)
hashtable.show()
hashtable.put(44)
hashtable.show()
hashtable.put(108)
hashtable.show()
hashtable.put(97)
hashtable.show()
hashtable.put(86)
hashtable.show()
