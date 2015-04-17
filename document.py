class NO_TEXT_FOUND(Exception):
  pass

class Document:
  # initializer
  def __init__(self, text=None, filename=None):
    # if text is None, initialize using filename
    # if filename is None, initialize using text
    # if both are None, throw exception
    # text, filename are of type String
    if text == None:
      if filename == None:
        raise NO_TEXT_FOUND("Neither text nor file found")
      else: self.text = open(filename, 'r').read()
    else: self.text = text

  # tokenizer
  def tokenize(self, delimiter=' '):
    # tokenize the string using an optional delimiter
    # del is of type String
    return self.text.split(delimiter)