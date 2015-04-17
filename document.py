class Document:
  # initializer
  def __init__(self, text=None, filename=None):
    # if text is None, initialize using filename
    # if filename is None, initialize using text
    # if both are None, throw exception
    # text, filename are of type String
    if text = None:
      if filename = None:
        throw exception
      else self.text = open(filename, 'r').read()
    else self.text = text

  # tokenizer
  def tokenize(del=" "):
    # tokenize the string using an optional delimiter
    # del is of type String
    return self.text.split(del)