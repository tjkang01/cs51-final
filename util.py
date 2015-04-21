# class of utility functions
class Util:
  @staticmethod
  def tokenize(text):
    # remove new line characters
    tokens = text.replace("\n", "")
    # split with space delimiter
    tokens = tokens.split(" ")
    # filter out empty strings
    tokens = filter(None, tokens)
    #return tokens
    return tokens

  @staticmethod
  def strip(line):
    # remove new line characters
    clean = line.replace("\n", "")
    # remove extra whitespace
    clean = clean.strip()
    #return stripped line
    return clean

  @staticmethod
  def open_file(filename):
    # try to open the file
    try:
      f = open(filename, 'r')
    # if an exception is thrown...
    except IOError:
      # print our an error and return nothing
      print "File " + filename + " does not exist."
      return None
    # otherwise return the new file buffer
    return f