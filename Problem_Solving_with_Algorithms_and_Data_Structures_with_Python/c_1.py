
# the infinite monkey theorem
'''
import string
import random


target = "methinks it is like a weasel"

alphabet = list(string.ascii_lowercase)
alphabet.append(' ')




def generate_random_string(dic):
   random_string = []
   for i in range(28):
      if i in dic:
         letter = dic[i]
         random_string.append(letter)
      else:
         letter = random.choice(alphabet)
         random_string.append(letter)

   return ''.join(random_string)

#

# print(random_string)
def score_random_string(target, random, dic):

   correct = 0
   wrong = 0

   for i in range(len(target)):

      if target[i] == random[i]:
         correct += 1
         dic[i]=target[i]
      else:
         wrong += 1

   return (correct/ (correct + wrong) * 100), dic


score = 0
iterations = 0
dic = {}
while score < 100:
   iterations +=1
   # print(dic)
   random_string = generate_random_string(dic)
   new_score, new_dic = score_random_string(target, random_string, dic)
   for k in new_dic:
      if k not in dic:
         dic[k] = new_dic[k]
   # print(dic)
   if new_score > score:
      score = new_score
      print(score)
      print(random_string)

   if iterations % 10000 == 0:
      print(iterations)
'''

# classes

# example 1 FRACTIONS
'''
def gcd(m, n):
   while m % n != 0:
      old_m = m
      old_n = n
      m = old_n
      n = old_m % old_n
   return n




# gcd function
def gcd(m, n):
   while m % n != 0:
      old_m = m
      old_n = n
      m = old_n
      n = old_m % old_n
   return n

# Fraction class
# Implements: addition and equality
# To do: multiplication, division, subtraction and comparison operators (< , >)
class Fraction:
    def __init__(self, top, bottom):
       if isinstance(top, int) and isinstance(bottom, int):
          self.num = top
          self.den = bottom
          common = gcd(self.num, self.den)
          self.num = self.num // common
          self.den= self.den// common
       else:
          raise ValueError("num/den is not integer")

    def __str__(self):
       return str(self.num) + "/" + str(self.den)

    def show(self):
       print(self.num, "/", self.den)

    def __add__(self, other_fraction):
       new_num = self.num * other_fraction.den + \
                self.den * other_fraction.num
       new_den = self.den * other_fraction.den
       common = gcd(new_num, new_den)
       return Fraction(new_num // common, new_den // common)

    def __radd__(self, other_fraction):
       new_num = self.num * other_fraction.den + \
                self.den * other_fraction.num
       new_den = self.den * other_fraction.den
       common = gcd(new_num, new_den)
       return Fraction(new_num // common, new_den // common)

    def __eq__(self, other):
       first_num = self.num * other.den
       second_num = other.num * self.den
       return first_num == second_num
    
    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return str(num) + "/" + str(den)

    def get_num(self):
         return self.num

    def get_den(self):
         return self.den



f1 = Fraction(1, -5)
f2 = Fraction(1, -2)
f3 = f1 + f2

print(f3)
'''

# Write two Python functions to find the minimum number in a list.
# The first function should compare each number to every other number on the list. O(n2).
# The second function should be linear O(n)


