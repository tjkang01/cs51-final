# 1a. Write a method that takes in a .txt file (e.g. example_seed.txt), and creates a String:[Document] dictionary.  
# For every "file1a.txt", create a new Document file.  
# You can use a simple array, since we need to traverse every Document and it'll be O(n) no matter what.  
# Whoever does this part can also do part 2a, since the method will be useful in completing this task.

from document import Document
from util import Util

# seed is the name of the seed file
def create_dict(seed):
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
  # return dictionary
  return dict