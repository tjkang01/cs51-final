class Analyzer:
  # utility class, hidden from users
  class Heuristic:
    # initializer
    def __init__(self, opt, text):
      # initialize the Heuristic using the heuristic’s name (opt) and combined text (text) of all of the documents in the seed 
      # opt, text are of type String
    
    # updater
    def update(self, doc):
      # update the stored values with a new document
      # doc is of type Document
  
  # initializer
  def __init__(self, seed):
    # initialize the object
    # seed is of type Seed
  
  # updater
  def update(self, opt, doc):
    # update stored values using a new doc
    # opt is of type String
    # doc is of type Document
  
  # analyzer
  def analyze(self, doc):
    # analyze a new document using the stored values
    # needs to output the probabilities of each of the stored heuristics, ranked from highest to lowest probability
    # doc is of type Document