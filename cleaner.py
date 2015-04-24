from util import Util
import re
import string

def format(file):
  # review is the name of the file that will be cleaned
  # open the review file
  f = open(file, "r")
  # begin reading
  # number of reviews; tracker
  number = 0
  for line in f:
    # only gets the actual review
    if "review/text" in line:
      # increments
      number += 1
      # gets rid of the review
      temp = line.replace("review/text:", "")
      # turns the review into a tokenized list
      words = Util.tokenize(temp)
      # creates new file with incremented number
      fi = open(str(number) + ".txt", "w")
      # for each word in the review...
      for word in words:
        # only adds words that meet the follow regular pattern
        if (re.compile("^[a-zA-Z'-]+$")).match(word):
          # add the word to the file
          fi.write(word + " ")
      # close the file
      fi.close()