from document import Document
from util import Util
from alphatree import AlphaTree

# analyzer class
class Analyzer:
  # initializer
  def __init__(self, seed):
    # seed is the name of the seed file
    # initialize an empty dictionary
    dict = {}
    # open the seed file
    f = Util.open_file(seed)
    # begin reading
    while True :
      # read heuristic line
      line = f.readline()
      # quit if end of file
      if not line : break
      # store new heuristic
      current_heuristic = Util.strip(line)
      # read filenames
      filenames = f.readline()
      # if there isn't another line, quit - incorrect syntax
      if not filenames : 
        print ("Incorrect seed structure.  Exiting")
        sys.exit()
      # store tokens
      filenames = Util.tokenize(filenames)
      # create document array variable
      docs = []
      # iterate over files
      for file in filenames :
        # try to open the file
        new_doc = Document(None, file)
        # if the new document's text is successfuly initialized...
        if new_doc.text :  
          # add it to the array
          docs.append(new_doc)
      # add new heuristic and docs to dict
      dict[current_heuristic] = docs
      # store dictionary
      self.dict = dict

    # calculate required values
    self.consolidate()
    self.transform()
  
  # setup method - convert dicts of String:[Document] into alphatrees
  def consolidate(self):
    self.word_counts = {}
    for key in self.dict.keys():
      print key
      new_tree = AlphaTree()
      for doc in self.dict[key]:
        for word in doc.tokenize():
          new_tree.add(word)
      self.word_counts[key] = new_tree

  # calculate log-transformed tree
  def transform(self):
    self.log_values = {}
    for key in self.word_counts.keys():
      self.log_values[key] = self.word_counts[key].calc_values()

  # analyzer
  #def analyze(self, doc):
    # analyze a new document using the stored values
    # doc is of type Document