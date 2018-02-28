# ******************
#      RECURSION
# ******************

from c_3_study import Queue
# example from book
def list_sum(num_list):
  print(num_list)
  if len(num_list) == 1:
      print('len 1')
      return num_list[0]

  else:
      print('len', len(num_list))
      print(num_list[0])
      print(num_list[1:])
      return num_list[0] + list_sum(num_list[1:])


# print(list_sum([1,3,5,7,9]))

# example from internet
def factorial(n):
    print("factorial has been called with n = " + str(n))
    print(n)
    if n == 1:
        print('1')
        return 1
    else:

        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res

# print(factorial(4))
#
# explanation:
# calc_factorial(4)              # 1st call with 4
# 4 * calc_factorial(3)          # 2nd call with 3
# 4 * 3 * calc_factorial(2)      # 3rd call with 2
# 4 * 3 * 2 * calc_factorial(1)  # 4th call with 1
# 4 * 3 * 2 * 1                  # return from 4th call as number=1
# 4 * 3 * 2                      # return from 3rd call
# 4 * 6                          # return from 2nd call
# 24                             # return from 1st call


# example from book

def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[int(n)]
    else:
        return to_str(int(n) / base, base) + convert_string[int(n) % base]


# print(to_str(769, 10))

import turtle
my_turtle = turtle.Turtle()
my_win = turtle.Screen()
def draw_spiral(my_turtle, line_len):
   if line_len > 0:
      my_turtle.forward(line_len)
      # my_turtle.left(90)
      draw_spiral(my_turtle, line_len - 5)

draw_spiral(my_turtle, 100)
my_win.exitonclick()