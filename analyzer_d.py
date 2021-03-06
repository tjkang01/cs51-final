from document import Document
from util import Util
from alphatree import AlphaTree
import glob
import os

# analyzer class
class Analyzer:
  # string representations for clarification
  def __repr__(self):
    return "Analyzer"
  def __str__(self):
    str_repr = ""
    for key in self.log_values:
      str_repr += key + "-" * (47 - len(key)) + "\n  "
      str_repr += self.log_values[key].__str__().replace("\n", "\n  ")[:-2]
    return str_repr

  # initializer
  def __init__(self, seed=None):
    # if no seed is provided, return an error
    if seed == None:
      print "Initializing an Analyzer object requires a seed.  Please try again."
      return
    # initialize an empty dictionary
    dict = {}
    # ---USER FEEDBACK---
    print "\nAttempting to read seed file..."
    # open the seed file
    f = Util.open_file(seed)
    # if the file doesn't exist, return
    if not f:
      print "Initialization failed; please verify that the seed exists then try again."
      return
    # begin reading
    while True :
      # read heuristic line
      line = f.readline()
      # quit if end of file
      if not line : break
      # store new heuristic
      current_heuristic = Util.strip(line)
      # ---USER FEEDBACK---
      print "Reading files for heuristic \'" + current_heuristic + "\'..."
      # read filenames
      next_line = f.readline()
      # if there isn't another line, quit - incorrect syntax
      if not next_line : 
        print ("Incorrect seed structure.  Exiting")
        sys.exit()
      # try to store number of files for this heuristic
      try:
        num_files = int(next_line)
      # if an exception is thrown...
      except ValueError:
        # print out an error and return nothing
        print "Seed file is of incorrect format.  Please try again."
        return
      # create document array variable
      docs = []
      # iterate over files
      for i in range(num_files) :
        # try to open the file
        filename = current_heuristic + "/" + str(i) + ".txt"
        new_doc = Document(None, filename)
        # if the new document's text is successfuly initialized...
        if new_doc.text :  
          # add it to the array
          docs.append(new_doc)
      # add new heuristic and docs to dict
      dict[current_heuristic] = docs
      # store dictionary
      self.dict = dict

    # ---USER FEEDBACK---
    print "Done reading files!\n"

    # calculate required values
    # initialize dictionaries
    self.word_counts = {}
    self.log_values = {}
    # analyze for each heuristic found
    for key in self.dict:
      self.consolidate(key)
      self.transform(key, True)

    # ---USER FEEDBACK---
    print "Analyzer object initialized!\n"
  
  # setup method - convert dicts of String:[Document] into alphatrees
  def consolidate(self, key):
    # ---USER FEEDBACK---
    print "Consolidating files into word dictionaries..."
    # initialize a new tree
    new_tree = AlphaTree()
    # add all docs to the tree
    for doc in self.dict[key]:
      # add each word in the document
      for word in doc.tokenize():
        new_tree.add(word)
    # set the new tree for the given key
    self.word_counts[key] = new_tree

  # calculate log-transformed tree
  def transform(self, key, feedback):
    # ---USER FEEDBACK---
    # if the feedback tag is active, print out information
    if feedback:
      print "Calculating word probabilities for heuristic \'" + key + "\'...\n"
    # calculate tree statistics
    num_unique = self.word_counts[key].num_elements()
    total_words = self.word_counts[key].sum()
    # add new transformed tree to dictionary
    self.log_values[key] = self.word_counts[key].transform(num_unique, total_words)

  # analyzer
  def analyze(self, filename=None, text=None):
    # analyze a new document using the stored values
    # if there is a filename given, create a new Document object
    if filename != None:
      doc = Document(None, filename)
      words = doc.tokenize()
    # otherwise, analyze the given text
    elif text != None:
      words = Util.tokenize(text)
    # if both are None, return error
    else:
      print "Analyzer requires a filename or text to analyze.  Please try again."
      return
    # store dict of log value sums
    log_sums = {}
    # for every heuristic...
    for key in self.log_values:
      # initialize a value to 0
      current_sum = 0.0
      # iterate over words
      for word in words:
        current_sum += self.log_values[key].get(word)
      # store new sum
      log_sums[key] = current_sum
    
    # calculate largest log sum; this can be improved by doing this inside above loop
    # for clarity, we will add an extra loop here
    # track largest sum
    largest = -1.0
    # track largest key
    largest_heuristic = ""
    # iterate through all the keys
    for key in log_sums:
      # if the new value is larger...
      if log_sums[key] > largest:
        # update values
        largest = log_sums[key]
        largest_heuristic = key
    # return best key
    return largest_heuristic

  # method to add a document to storage
  def add(self, doc, heuristic, tagged):
    # tokenize document content
    words = doc.tokenize()
    # if the document was tagged with the correct heuristic, remove the first word
    if tagged:
      words.pop(0)
    # iterate over the words
    for word in words:
      # add word to correct alphatree
      self.word_counts[heuristic].add(word)
    # recalculate new values
    self.transform(heuristic, False)

  # utility print statements
  def show_logs(self):
    print self.__str__()
  def show_counts(self):
    str_repr = ""
    for key in self.word_counts:
      str_repr += key + "-" * (36 - len(key)) + "\n  "
      str_repr += self.word_counts[key].__str__().replace("\n", "\n  ")[:-2]
    print str_repr

  # MACHINE LEARNING METHODS
    # the same documents will be used for both
    # in one method, the program will be told the file heuristic after it guesses
    # in the other, the program will not be told the heuristic (real life)
    # output percentage correctness in both cases into file

  # learning sequence 1 - analyzer learns given categorized documents
  def learn(self, dir, easy):
    # in this sequence, labeled documents are provided
    # dir is the filename of the directory containing the labeled documents
    # in labeled documents, the first line is the heuristic and the second is the text
    # if easy is True, we allow the program to learn based on the correct heuristic
    # if easy is False, the analyzer will assume its guess is correct

    # get total number of files in directory
    num_files = sum(os.path.isfile(f) for f in glob.glob(dir + "/*"))
    # tracker to store number of correct guesses so far
    total_correct = 0
    # total correctly formatted files so far
    total_files = 0
    # document names should be formatted as "n.txt", where n goes from 0 to num_files - 1
    for i in range(num_files):
      # filename
      fn = dir + "/" + str(i) + ".txt"
      # open the new file
      f = Util.open_file(fn)
      # if the file is not None (i.e. opening the file was successful)
      if f:
        # calculate correct and guessed heuristics
        correct_heuristic = f.readline()[:-1]
        text = f.readline()
        guessed_heuristic = self.analyze(None, text)
        # token to show user whether program guessed correctly or not
        was_correct = "N"
        # if the two are equal...
        if correct_heuristic == guessed_heuristic:
          # change token to yes
          was_correct = "Y"
          # increment total correct
          total_correct += 1
        # increment total files
        total_files += 1
        # add new document to dictionaries
        if easy:
          self.add(Document(None, fn), correct_heuristic, True)
        else:
          self.add(Document(None, fn), guessed_heuristic, True)
        # print results
        print "File " + str(i) + ": " + was_correct + ". " + str(total_correct) + "/" + str(total_files)