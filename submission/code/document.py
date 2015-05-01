from util import Util

class NO_TEXT_FOUND(Exception):
  pass

class Document:
  # methods to help clarify print statements
  def __repr__(self):
    return "Document"
  def __str__(self):
    return self.text

  # initializer
  def __init__(self, text=None, filename=None):
    # if text is None, initialize using filename
    # if filename is None, initialize using text
    # if both are None, throw exception
    # text, filename are of type String
    if text == None:
      if filename == None:
        print "File not found: " + filename
      else: self.text = self.strip(Util.open_file(filename).read())
    else: self.text = self.strip(text)

  # tokenizer
  def tokenize(self, delimiter=" "):
    # tokenize the string using an optional delimiter
    # del is of type String
    return Util.tokenize(self.text)

  # newline stripper
  @staticmethod
  def strip(text) :
    # replace newline characters with spaces
    return text.replace("\n", " ")