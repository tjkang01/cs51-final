from util import Util
import re
import string

def format(file, max_r):
  # review is the name of the file that will be cleaned
  # open the review file
  f = open(file, "r")
  # begin reading
  # number of reviews
  number1 = 0
  number2 = 0
  # initialize counters
  counter1 = -1
  counter2 = -1
  for line in f:
    # break if we already have all the reviews we want
    if number1 == max_r and number2 == max_r:
      break;
    # only gets the actual review
    if "review/score" in line:
      score = line.replace("review/score: ", "")
      score = float(score)
      score = int(score)
      if score == 1 : 
        counter1 = 3
      elif score == 5 : 
        counter2 = 3 
    elif counter1 == 0 and number1 < max_r:
      # gets rid of the review
      temp = line.replace("review/text:", "")
      # turns the review into a tokenized list
      words = Util.tokenize(temp)
      # creates new file with incremented number
      f = open("negative/" + str(number1) + ".txt", "w")
      # increments
      number1 += 1
      # print out words
      for word in words:
        # only adds words that meet the follow regular pattern
        if (re.compile("^[a-zA-Z'-]+$")).match(word):
          f.write(word + " ")
      f.close()
    elif counter2 == 0 and number2 < max_r:
      # gets rid of the review
      temp = line.replace("review/text:", "")
      # turns the review into a tokenized list
      words = Util.tokenize(temp)
      # creates new file with incremented number
      f = open("positive/" + str(number2) + ".txt","w")
      # increments
      number2 += 1
      # print out words
      for word in words:
        # only adds words that meet the follow regular pattern
        if (re.compile("^[a-zA-Z'-]+$")).match(word):
          f.write(word + " ")
      f.close() 
    # if either counter is nonnegative, decrement
    if counter1 > -1:
      counter1 -= 1
    if counter2 > -1:
      counter2 -= 1
  s = open("seed.txt", "w")
  s.write("positive\n" + str(number1) + "\n")
  s.write("negative\n" + str(number2))
  s.close()