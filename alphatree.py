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
    str_repr = ""
    for i in range(0, 27):
      c = AlphaTree.alphabet[i]
      if tree.values[i] > 0:
        str_repr += prefix + c + ": " + str(tree.values[i]) + "\n"
      if tree.table != []:
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
        return 27
      elif l == '-':
        return 28
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
    for i in range(0, 27):
      sum += self.values[i]
    # if the table is not empty, recurse through subtrees
    if self.table != []:
      for i in range(0, 27):
        sum += self.table[i].sum()
    return sum

  # get total number of vals
  def num_elements(self):
    # store the total
    total = 0.0
    # iterate over values
    for i in range(0, 27):
      if self.values[i] > 0:
        total += 1.0
    # if the table is not empty, recurse through subtrees
    if self.table != []:
      for i in range(0, 27):
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
      return self.table[i].get(str[1:])

  # add an entry
  def add(self, str, val=None):
    # if the str is not a match, return
    if not AlphaTree.check(str):
      return
    # get array index of first letter
    i = AlphaTree.indexof(str[0])
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
        for j in range(1, 28):
          self.table.append(AlphaTree())
      self.table[i].add(str[1:], val)

  # return Bayesian transformed tree
  def calc_values(self):
    counter = True
    log_tree = copy.deepcopy(self)
    vocab_size = self.num_elements()
    print "Vocab size: " + str(vocab_size)
    total_words = self.sum()
    print "Total words: " + str(total_words)
    for i in range(0, 27):
      if self.values[i] != 0:
        if counter:
          print self.values[i]
          print total_words + vocab_size
          counter = False
        log_tree.values[i] = math.log10(self.values[i] + 1) - math.log10(total_words + vocab_size)
        print log_tree.values[i]
      else:
        log_tree.values[i] = 0.0
    for i in range(0, 27):
      if self.table != []:
        log_tree.table[i] = self.table[i].calc_values()
      else:
        log_tree.table = []
    return log_tree