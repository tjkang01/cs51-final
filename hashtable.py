import analyzer from Analyzer

class HashTable:
  # initializer
  def __init__(self):
    # create initial hashtable with all empty entries (e.g. 28 HashTable array with zeroed entries)
    # entries should be of any type (we will be using ints and floats)

    # display this information as a nested dictionary {heuristic: {word: int, word: int, word: int}
    # it needs to be a nested dicitonary because we have a value associated with every key (word)

    # initialize an empty dictionary that will contain the desired {heuristic: {word: int, word: int, word: int}
    heruistic_dict = {} 
    # initialize an empty dictionary that will contain the nested dictionary 
    word_and_count = {} 
    # import the dictionary made from the analyzer file that has {heuristic : [doc1,doc2,doc3...]}
    initial_dict = Analyzer.dictionary 
    # extract just the doc objects [doc1, doc2 ...]
    doc_list = initial_dict.values()[0]
    # keeps count of all the words
    count = {} 
    # iterate over the list of doc objects
    for i in range(0, len(doc_list)):
    	words[i] = doc_list[i]    
    		# checks each word in each document object and increases the count for the word if it has already been passed	
		    for word in words[i]:
		    	if word in count: 
		    		count[word] += 1
		    	else:
		    		count[word] = 1     
		# creates a dictionary using the word and the count in the format: word_and_count = {'word' : 1, 'word2' : 43 ...}    				
		word_and_count[word] = count[word]    	
    # sets the key (the current_heuristic) equal to the value, which, in this case, is the nested dictionary 
    heuristic_dict[Analyzer.current_heuristic] = word_and_count

  # accessor methods
  def get(self, word):
    # return value for a given word (e.g. 0 occurrences, log is 0.223, etc)

  def add(self, val=None):
    # method to add in a new value to the HashTable (e.g. a new word)