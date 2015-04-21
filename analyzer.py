from document import Document
from util import Util

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
  
  # updater
  # def update(self, opt, doc):
    # update stored values using a new doc
    # opt is of type String
    # doc is of type Document
  
  # analyzer
  # def analyze(self, doc):
    # analyze a new document using the stored values
    # needs to output the probabilities of each of the stored heuristics, ranked from highest to lowest probability
    # doc is of type Document