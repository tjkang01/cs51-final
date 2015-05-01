import re
import itertools
import string
import copy
import math

# The AlphaTree class has a array of length 29.  The first 26 entries correspond to the letters A-Z.
# The 27th corresponds to ', and the 28th corresponds to -.  The 29th entry stores a value
# describing the word; in some cases it will be an integer storing the # of occurrences, and in others
# it will be the log of the probability calculated during the Naive Bayes algorithm.  The add method
# allows for this variation in type of value.
class AlphaTree:
  # regex tester for matching words
  matcher = re.compile("^[a-zA-Z'-]+$")
  # word alphabet
  alphabet = list(string.ascii_lowercase)
  alphabet.append('\'')
  alphabet.append('-')

  # methods to help clarify print statements
  def __repr__(self):
    return "AlphaTree"
  def __str__(self):
    return AlphaTree.to_string(self, "")

  @staticmethod
  # utility tostring function
  def to_string(tree, prefix):
    # initial string
    str_repr = ""
    # for each of the 28 values
    for i in range(28):
      # get first letter
      c = AlphaTree.alphabet[i]
      # if there are additional letters
      if tree.values[i] != 0:
        # format each line to have same tab length - look like a table
        num_spaces = 30 - len(prefix + c + ": ")
        # add the next word
        str_repr += prefix + c + ": " + (" " * num_spaces) + str(tree.values[i]) + "\n"
      # if there are subsequent words
      if tree.table != []:
        # add in the subtree's words
        str_repr += AlphaTree.to_string(tree.table[i], prefix + c)
    return str_repr

  # initializer
  def __init__(self):
    # create empty array
    self.table = []
    self.values = list(itertools.repeat(0.0, 28))

  @staticmethod
  # convert a letter into an index
  def indexof(l):
    if len(l) != 1 :
      return -1
    else :
      if l.isalpha():
        return ord(l.lower()) - 97
      elif l == '\'':
        return 26
      elif l == '-':
        return 27
      else:
        return -1

  @staticmethod
  # check whether a word has correct characters
  def check(str):
    return AlphaTree.matcher.match(str)

  # return the sum of the values throughout the tree
  def sum(self):
    # store the sum
    sum = 0
    # iterate over values
    for i in range(28):
      sum += self.values[i]
    # if the table is not empty, recurse through subtrees
    if self.table != []:
      for i in range(28):
        sum += self.table[i].sum()
    return sum

  # get total number of vals
  def num_elements(self):
    # store the total
    total = 0.0
    # iterate over values
    for i in range(28):
      if self.values[i] > 0:
        total += 1.0
    # if the table is not empty, recurse through subtrees
    if self.table != []:
      for i in range(28):
        total += self.table[i].num_elements()
    return total

  # get the value for a given word
  def get(self, str):
    # if the str is not a match, return 0
    if not AlphaTree.check(str):
      return 0.0
    # get array index of first letter
    i = AlphaTree.indexof(str[0])
    # if the string is just a letter, return the appropriate value
    if len(str) == 1:
      return self.values[i]
    # if the string is not just a letter, get the rest of the string from the appropriate AlphaTree
    else:
      # if the table is empty, return zero
      if self.table == []:
        return 0.0
      # else return the next iteration
      return self.table[i].get(str[1:])

  # add an entry
  def add(self, str, val=None):
    # if the str is not a match, return
    if not AlphaTree.check(str):
      return
    # get array index of first letter
    i = AlphaTree.indexof(str[0])
    # if i is -1, the word's not a word we want to examine
    if i == -1:
      return
    # if the string is just a letter, add the approriate value
    if len(str) == 1:
      if val:
        self.values[i] += val
      else:
        self.values[i] += 1.0
    # if the string is not just a letter, add the rest of the string to the approriate AlphaTree
    else:
      # initialize table array if necessary
      if self.table == []:
        for j in range(28):
          self.table.append(AlphaTree())
      # add substring to subtree
      self.table[0].add(str[1:], val)

  # return Bayesian transformed tree
  def transform(self, num, total):
    # after initialization, all values are 0 and the table is []
    transformed = AlphaTree()
    # if current table is empty, no need to do anything for the table
    if self.table != []:
      # otherwise, substitute recursively transformed AlphaTrees
      for i in range(28):
        transformed.table.append(self.table[i].transform(num, total))
    # substitute appropriate values
    for i in range(28):
      # if the value is not zero, substitute in Bayesian value
      if self.values[i] != 0.0:
        transformed.values[i] = -1.0 * (math.log10(self.values[i] + 1) - math.log10(num + total))
      # otherwise, no need to do anything
    # return new tree
    return transformed

  # utility print statements
  def show(self):
    print self.__str__()