from document import Document
from util import Util
from alphatree import AlphaTree

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
    print "Attempting to read seed file..."
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
    print "Done reading files!"

    # calculate required values
    self.consolidate()
    self.transform()

    # ---USER FEEDBACK---
    print "Analyzer object initialized!"
  
  # setup method - convert dicts of String:[Document] into alphatrees
  def consolidate(self):
    # initialize word count dictionary
    self.word_counts = {}
    # ---USER FEEDBACK---
    print "Consolidating files into word dictionaries..."
    # for each heuristic...
    for key in self.dict.keys():
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
  def transform(self):
    # initialize log value dictionary
    self.log_values = {}
    # for each key in the dictionary...
    for key in self.word_counts.keys():
      # ---USER FEEDBACK---
      print "Calculating word probabilities for heuristic \'" + key + "\'..."
      # calculate tree statistics
      num_unique = self.word_counts[key].num_elements()
      total_words = self.word_counts[key].sum()
      # add new transformed tree to dictionary
      self.log_values[key] = self.word_counts[key].transform(num_unique, total_words)

  # analyzer
  def analyze(self, filename):
    # analyze a new document using the stored values
    doc = Document(None, filename)
    # get words from doc
    words = doc.tokenize()
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
    # print out new dictionary
    print log_sums

  # utility print statements
  def show_logs(self):
    print self.__str__()
  def show_counts(self):
    str_repr = ""
    for key in self.word_counts:
      str_repr += key + "-" * (36 - len(key)) + "\n  "
      str_repr += self.word_counts[key].__str__().replace("\n", "\n  ")[:-2]
    print str_repr