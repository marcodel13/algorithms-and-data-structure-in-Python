# ******************
#       STACKS
# ******************
# what is a stack:
# linear data structure, based on the LIFO principle.
# main methods: is_empty, length, pop, add, pick

# implement a stack


class Stack():

    def __init__(self):

        self.s = []
        self.min = None

    def is_empty(self):
        return self.length() == 0

    def size(self):
        return len(self.s)

    def pop(self):
        return self.s.pop()

    def pop_zero(self):
        return self.s.pop(0)

    def pop_modified(self):

        if self.s.pop()[1] == self.min:
            self.min = self.s[-1][1]

        # print(self.min)

    def push(self, item):
        self.s.append(item)

    def push_modified(self, item):

        # keep the minimum: if the stack is empty, the new item is the minimum
        if self.min == None:
            self.s.append((item, item))
            self.min = item
        # otherwise, compare it with the actual minimum
        elif item < self.min:
            self.s.append((item, item))
            self.min = item
        else:
            self.s.append((item, self.min))

        # print(self.min)

    def pick(self):
        return self.s[-1]

    def show(self):
        return (self.s)

    def get_min(self):
        print(self.min)


class SetOfStacks():

    def __init__(self):
        self.single_stack = Stack()
        self.max = 3
        self.stored_stacks = []


    def pop(self):
        if self.single_stack.size() > 0:
            item = self.single_stack.pop()
            return item
        else:
            print('stack is empty!')

    def popAt(self, index):

        # first version
        '''
        if len(self.stored_stacks[index]) > 0:
            item = self.stored_stacks[index].pop()
        else:
            print('stack at index {0} is empty!'.format(index))
        return item
        '''
        # rolling over version

        item = self.stored_stacks[index].pop()

        for i, s in enumerate(self.stored_stacks):
            try:
                if s.size() < self.max:
                    x = self.stored_stacks[i+1].pop_zero()
                    self.stored_stacks[i].push(x)
            except IndexError:
                print('got to the last stack')
                self.stored_stacks[i].push(self.single_stack.pop())


        return item

    def push(self, item):
        if self.single_stack.size() <= self.max -1 :

            self.single_stack.push(item)

        else:
            self.stored_stacks.append(self.single_stack)

            self.single_stack = Stack()
            self.single_stack.push(item)

    def show_sos(self):
        print('current stack', self.single_stack.show())

        if len(self.stored_stacks) > 0:
            for s in self.stored_stacks:
                print(s.show())
        else:
            print('no stored stacks')



# set_of_stacks_obj = SetOfStacks()

# for i in range(10):
#     set_of_stacks_obj.push(i)
#
# set_of_stacks_obj.show_sos()

# for i in range(10):
#     set_of_stacks_obj.push(i)
#     set_of_stacks_obj.show_sos()

# set_of_stacks_obj.pop()
# set_of_stacks_obj.show()
# set_of_stacks_obj.popAt(0)
# set_of_stacks_obj.show_sos()
# set_of_stacks_obj.popAt(1)
# set_of_stacks_obj.show()
# set_of_stacks_obj.popAt(1)
# set_of_stacks_obj.show()
# set_of_stacks_obj.popAt(1)
# set_of_stacks_obj.show()
#
# from CCI
'''
3.2 How would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element?
1. Push, pop and min should all operate in O(1) time
- You can implement this by having each node in the stack keep track of the minimum be- neath itsel

3.3 Imagine a (literal) stack of plates
If the stack gets too high, it might topple Therefore, in real life, we would likely start a new stack when the previous stack exceeds
some threshold. Implement a data structure SetOfStacks that mimics this SetOfStacks should be composed of several stacks,
and should create a new stack once the previous one exceeds capacity SetOfStacks push() and SetOfStacks pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there were just a single stack)

Implement a function popAt(int index) which performs a pop operation on a specific sub-stack

now do that with a "rolling over" (i.e, no stack has to be below its capacity)

'''



# ******************
#       QUEUE
# ******************
# what is a queus:
# linear data structure, based on the FIFO principle.
# main methods: is_empty, length, pop, add, pick

# implement a queue

class Queue():

    def __init__(self):
        self.q = []

    def enqueue(self, item):
        self.q.insert(0, item) # big O = n

    def dequeue(self):
        item = self.q.pop() # big O = 1
        return item

    def size(self):
        return len(self.q)

    def is_empty(self):
        return len(self.q) == 0

    def show(self):
        print(self.q)


# from the book:
# Implement the Queue ADT, using a list such that the rear of the queue is at the end of the list.

class Inverse_Queue():

    def __init__(self):
        self.q = []

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        item = self.q.pop(0)
        return item

    def size(self):
        return len(self.q)

    def is_empty(self):
        return len(self.q) == 0

    def show(self):
        print(self.q)


'''
q = Queue()
iq = Inverse_Queue()

iq.enqueue(23)
iq.show()
iq.enqueue(98)
iq.show()
iq.enqueue(77)
iq.show()
iq.dequeue()
iq.show()

q.enqueue(23)
q.show()
q.enqueue(98)
q.show()
q.enqueue(77)
q.show()
q.dequeue()
q.show()
'''


# from the book
# It is possible to implement a queue such that both enqueue and dequeue have O(1) per-
# formance on average. In this case it means that most of the time enqueue and dequeue
# will be O(1) except in one particular circumstance where dequeue will be O(n).

# using a linked list?

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        self.previous = None

    def get_data(self): # just return the data
        return self.data

    def get_next(self): # just return the node which the current node is connected to
        return self.next

    def get_previous(self):
        return self.previous

    def set_data(self, new_data): # assign new data
        self.data = new_data

    def set_next(self, new_next): #  IMP: connect the next node, the one current node is linked to
        self.next = new_next

    def set_previous(self, new_previous): #  IMP: connect the next node, the one current node is linked to
        self.previous = new_previous

class UnorderedList:

    def __init__(self):
        self.head = None # just define which is th head of the list. no need for the rest, since nodes are connected
        self.last = None # add this new variable to make the append method O=1
        self.count = 0

    def is_empty(self):
        return self.head == None

    def add(self, item):

        self.count += 1

        temp = Node(item) # incapsulte any new item into the Node Class
        # in this implementation, we want new nodes to be the HEADS of the list, therefore

        if self.head == None:# i.e. if the list is empty

            self.head = temp  # we then define the new node as the new head
            self.last = self.head # there is one item now that is both head and last

        else:
            self.head.set_previous(temp)

            temp.set_next(self.head)  # we first connect the new node to the current head



            self.head = temp  # we then define the new node as the new head

    def size(self):
        # current = self.head
        # count = 0
        # while current != None: # remember that the value None is only for the last node in the list, which is not connected to anything
        #     count = count + 1
        #     current = current.get_next()
        #
        return self.count

    def search(self, item):
        current = self.head # start traversing from the head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next() # if not found, move to the next node
        return found

    def remove(self, item):
        self.count -= 1
        current = self.head
        previous = None # since current starts from the head, previous starts out with a value of None since there is no node before the head
        found = False
        stop = False

        while not found and not stop: # repeat here the search step. We assume that the value we want to remove is present, so we don't need the None (see above)


            if current.get_next() != None:

                if current.get_data() == item: # check whether the item stored in the current node is the item we wish to remove.
                    found = True # When found becomes True, current will be a reference to the node containing the item to be removed

                else: # here we are moving the current and the previous one step ahead
                    previous = current
                    current = current.get_next()
            else:
                print('item not in list')
                stop = True
        # below: special case, when the item to be removed happens to be the first item in the list,
        if previous == None: # in this specail casse, previous has not moved, so it is still == None
            self.head = current.get_next() # we change the head of the list the head of the list, to refer to the node after the current node, thus removing the first node from the linked list

        else:# here: we have found the target node to be removed, so what we do is simply to connect previous to next,
             # thus removing current from the chain of connections
            previous.set_next(current.get_next())

    def append(self, item):

        temp = Node(item)# incapsulate the new itam into a Node object

        # version with O=n
        '''
        current = self.head  # start traversing from the head

        while current.get_next() != None: # check that the next is not NONE (i.e. not the last in the list)
            current = current.get_next()  # if not None, move to the next node
        # you have traversed the whole list, and got to the last

        current.set_next(temp) # link the last to the new item
        '''

        # version with O=1
        old_last = self.last
        old_last.set_next(temp)
        self.last = temp


    def show(self):

        current = self.head # start traversing from the head
        last = self.last
        # print('\nhead', current.get_data())
        # print('last', last.get_data())

        l = []

        while current != None:
            l.append(current.get_data())
            current = current.get_next()
        print(l)

        return l

class New_Queue():

    def __init__(self):

        self.nq = UnorderedList()

    def enqueue(self, item):
        self.nq.add(item)

    def dequeue(self):
        if self.nq.size() > 1:
            pen = self.nq.last.get_previous() # define the item before the last (O=1)
            pen.set_next(None) # set the next to None - this way, you are automatically cutting off the current last
            self.nq.last = pen
        else:
            self.nq.head = None
            self.nq.last = None
            print('empty!')


    def show(self):
        self.nq.show()

'''
q = Queue()
nq = New_Queue()

nq.enqueue(1)
nq.show()
nq.enqueue(3)
nq.show()
nq.enqueue(5)
nq.show()
nq.enqueue(5)
nq.show()
nq.dequeue()
nq.show()
nq.dequeue()
nq.show()


nq.enqueue(15)
nq.show()
nq.dequeue()
nq.show()
nq.dequeue()
nq.show()
nq.enqueue(15)
nq.show()
'''


# from the book
# Modify the Hot Potato simulation to allow for a randomly chosen counting value so
# that each pass is not predictable from the previous one

import random

def Hot_Potato(list_names, max_num):

    q = Queue()


    # add everyone to the queue
    for p in list_names:
        q.enqueue(p)
    q.show()
    while q.size() > 1:
        # start the game
        for i in range(0, random.randint(1,max_num)):
            q.show()
            last_person = q.dequeue()

            q.enqueue(last_person)

        q.dequeue() # eliminate the last
    q.show()

# Hot_Potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)


# from book
# Write a program that can check an HTML document for proper opening and closing tags

class New_Stack():

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def show(self):
        print(self.stack)



def html_checker(input_formula):

    s = New_Stack()

    for item in input_formula.split():
        for char in list(item):

            if char== '<':
                s.push(item)
            elif char== '>':
                s.pop()

    if s.size() == 0:
        print('formula is balanced')
    else:
        print('formula is not balanced')


formula = "<html>      <head>         <title>           Example         </title>      </head>      <body>         <h1>Hello, world</h1>      </body>    </html>"

# html_checker(formula)

# from book
# To implement the length method, we counted the number of nodes in the list. An alter-
# native strategy would be to store the number of nodes in the list as an additional piece
# of data in the head of the list. Modify the UnorderedList class to include this information and rewrite the length method.

# from book
# Implement the remove method so that it works correctly in the case where the item is not in the list
class New_UnorderedList:

    def __init__(self):
        self.head = None # just define which is th head of the list. no need for the rest, since nodes are connected
        self.last = None # add this new variable to makw the append method O=1
        self.count = 0

    def is_empty(self):
        return self.head == None

    def add(self, item):
        self.count +=1
        temp = Node(item) # incapsulte any new item into the Node Class
        # in this implementation, we want new nodes to be the HEADS of the list, therefore
        temp.set_next(self.head) # we first connect the new node to the current head

        if self.head == None:
            self.head = temp  # we then define the new node as the new head
            self.last = self.head

        else:
            self.head = temp  # we then define the new node as the new head

    def size(self):
        # current = self.head
        # count = 0
        # while current != None: # remember that the value None is only for the last node in the list, which is not connected to anything
        #     count = count + 1
        #     current = current.get_next()

        return self.count

    def search(self, item):
        current = self.head # start traversing from the head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next() # if not found, move to the next node
        return found

    def remove(self, item):
        self.count -= 1
        current = self.head
        previous = None # since current starts from the head, previous starts out with a value of None since there is no node before the head
        found = False
        stop = False


        while not found and not stop: # repeat here the search step. We assume that the value we want to remove is present, so we don't need the None (see above)

            if current.get_data() == item: # check whether the item stored in the current node is the item we wish to remove.
                found = True # When found becomes True, current will be a reference to the node containing the item to be removed

            else: # here we are moving the current and the previous one step ahead
                previous = current
                if current.get_next() != None:
                    current = current.get_next()
                else:
                    print('item not in list!')
                    stop = True

        # below: special case, when the item to be removed happens to be the first item in the list,
        if previous == None: # in this specail casse, previous has not moved, so it is still == None
            self.head = current.get_next() # we change the head of the list the head of the list, to refer to the node after the current node, thus removing the first node from the linked list

        else:# here: we have found the target node to be removed, so what we do is simply to connect previous to next,
             # thus removing current from the chain of connections
            previous.set_next(current.get_next())

    def append(self, item):

        temp = Node(item)# incapsulate the new itam into a Node object

        # version with O=n
        '''
        current = self.head  # start traversing from the head

        while current.get_next() != None: # check that the next is not NONE (i.e. not the last in the list)
            current = current.get_next()  # if not None, move to the next node
        # you have traversed the whole list, and got to the last

        current.set_next(temp) # link the last to the new item
        '''

        # version with O=1
        old_last = self.last
        old_last.set_next(temp)
        self.last = temp


    def show(self):

        current = self.head # start traversing from the head
        last = self.last
        # print('\nhead', current.get_data())
        # print('last', last.get_data())

        l = []

        while current != None:
            l.append(current.get_data())
            current = current.get_next()
        return l


'''
# mylist = New_UnorderedList()
# mylist.add(31)
# mylist.add(32)
# mylist.add('a')
# mylist.add('b')

# print(mylist.show())
# mylist.remove(31)
# mylist.remove(33)
# print(mylist.size())
# mylist.add(77)
# print(mylist.show())
# mylist.add(17)
# print(mylist.show())
# mylist.append(5)
# print(mylist.show())
# mylist.append('a')
# print(mylist.show())
# mylist.remove('a')
# print(mylist.show())
# print(mylist.size())
'''

# from book
# Implement a stack using linked lists

# new definition of node and class takes from internet
class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node


class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = node() # create a new node
        new_node.data = data
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.

    def list_print(self):
        node = self.cur_node # cant point to ll!
        l = []
        while node:
            l.append(node.data)
            node = node.next
        print(l)


class Stack_Linked_List:

    def __init__(self):
        self.current = None

    def push(self, item):
        new_node = node() # create an empty node
        new_node.data = item # fill the data slot with the item
        new_node.next = self.current # connect the new node with the current
        self.current = new_node # set the new node as the current

    def pop(self):
        self.current = self.current.next

    def show(self):
        print(self.current.data)
        l = []
        node = self.current

        while node:
            l.append(node.data)
            node = node.next
        print(l)

# st_ll = Stack_Linked_List()
#
# st_ll.push(1)
# st_ll.show()
# st_ll.push(2)
# st_ll.show()
# st_ll.push(3)
# st_ll.show()
# st_ll.pop()
# st_ll.show()
# st_ll.pop()
# st_ll.show()


class Queue_Linked_List():

    def __init__(self):
        self.current = None

    def enqueue(self, item):
        new_node = node()
        new_node.data = item
        new_node.next = self.current
        self.current = new_node

    def dequeue(self):
        current = self.current
        n = current.next

        while n.next != None:

            current = current.next
            n = n.next
        current.next = None

    def show(self):
        print(self.current.data)
        node = self.current
        l = []
        while node:
            l.append(node.data)
            node = node.next
        print(l)

# q_ll = Queue_Linked_List()
# q_ll.enqueue(1)
# q_ll.show()
# q_ll.enqueue(2)
# q_ll.show()
# q_ll.enqueue(3)
# q_ll.show()
# q_ll.enqueue(4)
# q_ll.show()
# q_ll.enqueue(5)
# q_ll.show()
# q_ll.dequeue()
# q_ll.show()
# q_ll.dequeue()
# q_ll.show()
# q_ll.dequeue()
# q_ll.show()
