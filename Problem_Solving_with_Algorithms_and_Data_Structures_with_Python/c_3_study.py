# ******************
#       STACKS
# ******************

# define the Stack class.
'''
in Python, as in any object-oriented programming language, the implementation of choice for an abstract data type such as a stack
is the creation of a new class. The stack operations are implemented as methods.
'''
class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)


# # create a Stack object ad play around with it
#
# s = Stack()
# s.push(4)
# s.push('dog')

# Write a function rev_string(my_str) that uses a stack to reverse the characters in a string.
def rev_string(my_str):

    s = Stack()

    for i in list(my_str):

        s.push(i)

    while s.is_empty() == False:

        print(s.pop())


# parenthesis checker
import sys

def matches(open, close):
   opens = "([{"
   closes = ")]}"
   return opens.index(open) == closes.index(close)

# function that checks if the parentheses in a sequence of symbols are balanced or not
def par_checker(symbol_string):

    s = Stack()

    for item in list(symbol_string):



        if item in "([{":

            s.push(item)

        else:

            if item in ")]}":
                try:
                    if matches(s.peek(), item):

                        s.pop()
                except IndexError:
                    sys.exit('Error: Opening parenthesis is missing for = {0}'.format(item))

    if s.is_empty():
        print('balanced parenthesis')
    else:
        print('unbalanced parenthesis: closing parenthesis missing')

# function to transform decimal number in a binary one

b = 10
def divide_by_base(dec_number, base):

    s = Stack()

    while dec_number != 0:

        s.push(dec_number%base)
        dec_number = dec_number // base

    binary_number = []

    while s.is_empty() == False:
        binary_number.append(s.pop())

    return  ''.join([str(x) for x in binary_number])


def base_converter(dec_number, base):
   digits = "0123456789ABCDEF"
   rem_stack = Stack()
   while dec_number > 0:
      rem = dec_number % base
      rem_stack.push(rem)
      dec_number = dec_number // base
   new_string = ""
   while not rem_stack.is_empty():
      new_string = new_string + digits[rem_stack.pop()]
   return new_string
# print(base_converter(256, b))


# function to tokenize expressions

def expression_tokenizer(expression):

    s = Stack()

    output = []

    numbers = [str(x) for x in range(10)]

    for item in list(expression):

        if item in numbers:
            s.push(item)

        elif item == ' ':
            i = []
            while s.is_empty() == False:
                i.append(s.pop())

            i = list(reversed(i))
            if len(i) > 0:
                output.append(''.join(i))

        elif item in "+-/*":
            i = []
            while s.is_empty() == False:
                i.append(s.pop())

            i = list(reversed(i))
            if len(i) > 0:
                output.append(''.join(i))

            output.append(item)

        elif item in "()":
            i = []
            while s.is_empty() == False:
                i.append(s.pop())

            i = list(reversed(i))
            if len(i) > 0:
                output.append(''.join(i))

            output.append(item)

    return output

# General Infix-to-Postfix Conversion

def Infix_to_Postfix(input_infix):

    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    op_stack = Stack() # keep the operators
    output = [] # put the results
    operands = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # short list of operands
    operands_number = [str(x) for x in range(20)]

    input_infix = expression_tokenizer(input_infix)
    print(input_infix)
    for item in input_infix:

        try:
            int_item = int(item)
        except ValueError:
            print ("Not an int")


        if item in operands or item in operands_number:
            output.append(item)

        elif item == "(":
            op_stack.push(item)

        elif item == ")":
            top_token = op_stack.pop()
            output.append(top_token)
            while top_token != '(':
                output.append(top_token)
                top_token = op_stack.pop()

        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[item]):
                output.append(op_stack.pop())

            op_stack.push(item)

    while not op_stack.is_empty():
        output.append(op_stack.pop())

    return " ".join(output)

# print(Infix_to_Postfix('10 + 3 * 5/(16-4)'))

# Compute the result for a post fix operation

def Compute_Postfix(expression):

    op_stack = Stack()

    for item in expression.split():

        try:
            item = int(item)
            op_stack.push(item)
        except ValueError:

            second_operand = op_stack.pop()
            first_operand = op_stack.pop()

            if item == "+":
                op_stack.push(first_operand+second_operand)

            elif item == "*":
                op_stack.push(first_operand * second_operand)

            elif item == "-":
                op_stack.push(first_operand - second_operand)

            elif item == "/":
                op_stack.push(first_operand / second_operand)

    return op_stack.peek()

# Compute_Postfix('10 + 3 * 5/(16-4)')
# ******************
#       QUEUE
# ******************


class Queue():

    def __init__(self):
        self.items = [] # Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue

    def enqueue(self, item):
        self.items.insert(0, item)
        # self.items = [item] + self.items --> uglier version

    def dequeue(self):
        # self.items = self.items[0:-1]
        # return self.items[-1]
        return self.items.pop() # recall that pop not only returns the last item, but also modifies the lists, therefore is ok

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)



# We will implement a general simulation of Hot Potato

def Hot_Potato(list_names, num):

    q = Queue()

    # add everyone to the queue
    for p in list_names:
        q.enqueue(p)

    while q.size() >1:
        # start the game
        for i in range(num):

            last_person = q.dequeue()
            q.enqueue(last_person)

        q.dequeue() # eliminate the last
    q.show()

# Hot_Potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)


# Printing Tasks
import random

class Printer():

    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    # internal timer
    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1 # why -1?

            if self.time_remaining <= 0:
                self.current_task = None

    # busy or not - simple binary choice
    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate

class Task():

    # constructor
    def __init__(self, time):

        self.timestamp = time # timestamp represents the time that the task was created and placed in the printer queue
        self.pages = random.randint(1,20) # number of pages

    # two simple methods to return the timestamp and the number of pages
    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    # wait_time method can then be used to retrieve the amount of time spent in the queue before printing begins
    def wait_time(self, current_time):
        return current_time - self.timestamp


# ******************
#       DEQUE
# ******************


class Deque():

    def __init__(self):
        self.items = [] # Deque() creates a new queue that is empty. It needs no parameters and returns an empty queue

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()  # recall that pop not only returns the last item, but also modifies the lists, therefore is ok

    def remove_rear(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)

def Palindrome_Checker(string):

    d = Deque()


    for l in string:
        d.add_front(l)

    output = []

    # solution one
    '''
    while d.is_empty() == False:

        output.append(d.remove_front())


    if ''.join(output) == string:
        print('palindrome!')
    else:
        print('no palindrome')
    '''

    # solution 2

    while d.size() >=1:
        a = d.remove_front()
        b = d.remove_rear()
        if a != b:
            print('no palindrome')
            break
        if d.is_empty() or d.size()==1:
            print('palindrome')
            break


# Palindrome_Checker('radar')

# ******************
#    LINKED LIST
# ******************


# create the node

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self): # just return the data
        return self.data

    def get_next(self): # just return the node which the current node is connected to
        return self.next

    def set_data(self, new_data): # assign new data
        self.data = new_data

    def set_next(self, new_next): #  IMP: connect the next node, the one current node is linked to
        self.next = new_next



# create the linked list - unordered: no order based on the value of the items it includes (e.g.: unordered: 12, 4, 90, 27 / ordered (ascending): 4, 12, 27, 90)

class UnorderedList:

    def __init__(self):
        self.head = None # just define which is th head of the list. no need for the rest, since nodes are connected
        self.last = None # add this new variable to makw the append method O=1

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item) # incapsulte any new item into the Node Class
        # in this implementation, we want new nodes to be the HEADS of the list, therefore
        temp.set_next(self.head) # we first connect the new node to the current head

        if self.head == None:
            self.head = temp  # we then define the new node as the new head
            self.last = self.head

        else:
            self.head = temp  # we then define the new node as the new head

    def size(self):
        current = self.head
        count = 0
        while current != None: # remember that the value None is only for the last node in the list, which is not connected to anything
            count = count + 1
            current = current.get_next()

        return count

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
        current = self.head
        previous = None # since current starts from the head, previous starts out with a value of None since there is no node before the head
        found = False

        while not found: # repeat here the search step. We assume that the value we want to remove is present, so we don't need the None (see above)

            if current.get_data() == item: # check whether the item stored in the current node is the item we wish to remove.
                found = True # When found becomes True, current will be a reference to the node containing the item to be removed

            else: # here we are moving the current and the previous one step ahead
                previous = current
                current = current.get_next()
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
        print('\nhead', current.get_data())
        print('last', last.get_data())

        l = []

        while current != None:
            l.append(current.get_data())
            current = current.get_next()
        return l


# playing
# mylist = UnorderedList()
# mylist.add(31)
# print(mylist.show())
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


# create an Ordered linked list - unordered: no order based on the value of the items it includes (e.g.: unordered: 12, 4, 90, 27 / ordered (ascending): 4, 12, 27, 90)
class OrderedList:

    def __init__(self):
        self.head = None
        self.last = None

    def is_empty(self): # same as unordered
        return self.head == None

    def size(self): # same as unordered
        current = self.head
        count = 0
        while current != None: # remember that the value None is only for the last node in the list, which is not connected to anything
            count = count + 1
            current = current.get_next()
        return count

    def remove(self, item): # same as unordered
        current = self.head
        previous = None # since current starts from the head, previous starts out with a value of None since there is no node before the head
        found = False

        while not found: # repeat here the search step. We assume that the value we want to remove is present, so we don't need the None (see above)

            if current.get_data() == item: # check whether the item stored in the current node is the item we wish to remove.
                found = True # When found becomes True, current will be a reference to the node containing the item to be removed

            else: # here we are moving the current and the previous one step ahead
                previous = current
                current = current.get_next()
        # below: special case, when the item to be removed happens to be the first item in the list,
        if previous == None: # in this specail casse, previous has not moved, so it is still == None
            self.head = current.get_next() # we change the head of the list the head of the list, to refer to the node after the current node, thus removing the first node from the linked list

        else:# here: we have found the target node to be removed, so what we do is simply to connect previous to next,
             # thus removing current from the chain of connections
            previous.set_next(current.get_next())

    def search(self, item):
        current = self.head # start traversing from the head
        found = False

        while current <= item and current !=None and not found: # modified in order to leverage the fact that we are woring with an ordered list

            if current.get_data() == item:
                found = True
            else:
                current = current.get_next() # if not found, move to the next node
        return found

    def add(self, item):
        temp = Node(item) # incapsulte any new item into the Node Class

        current = self.head

        # first scenaro: the list is empty, therefore the new item becomes the head
        if current == None:
            self.head = temp

        # if list is not empty
        else:
            next = current.get_next()
            # second scenario: if the head is higher than the new item, the new item becomes the head
            if current.get_data() > temp.get_data():
                print('\n\nsecond scenario')
                temp.set_next(current)
                self.head = temp

            # third scenarion:
            else:
                print('\n\nthird scenario')
            # elif current.get_data() < temp.get_data():
                while current.get_data() < temp.get_data():

                    try:
                        if next.get_data() < temp.get_data():
                            current = next
                            next = next.get_next()

                        else:
                            current.set_next(temp)
                            temp.set_next(next)
                            break

                    except AttributeError:
                        current.set_next(temp)
                        break

    def show(self):

        current = self.head # start traversing from the head
        last = self.last
        print('head', current.get_data())

        l = []

        while current != None:
            l.append(current.get_data())
            current = current.get_next()
        return l


#
# myOrderedlist = OrderedList()
# myOrderedlist.add(6)
# print(myOrderedlist.show())
#
# myOrderedlist.add(4)
# print(myOrderedlist.show())
#
# myOrderedlist.add(2)
# print(myOrderedlist.show())
#
# myOrderedlist.add(3)
# print(myOrderedlist.show())
#
# myOrderedlist.add(5)
# print(myOrderedlist.show())
#
# myOrderedlist.add(7)
# print(myOrderedlist.show())
#
#
# myOrderedlist.add(100)
# print(myOrderedlist.show())
#
# myOrderedlist.add(1)
# print(myOrderedlist.show())
#
# myOrderedlist.add(50)
# print(myOrderedlist.show())
#
# myOrderedlist.add(500)
# print(myOrderedlist.show())
#
# myOrderedlist.add(6)
# print(myOrderedlist.show())