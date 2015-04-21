# 1a. Write a method that takes in a .txt file (e.g. example_seed.txt), and creates a String:[Document] dictionary.  
# For every "file1a.txt", create a new Document file.  
# You can use a simple array, since we need to traverse every Document and it'll be O(n) no matter what.  
# Whoever does this part can also do part 2a, since the method will be useful in completing this task.

def create_dict(h, txt):
# h is the name of the heuristic, as a string.
# txt is the text file containing the list of .txt files that need to be put into the dictionary.
	doc_list = []
	f = open(txt, "r")
	for line in f:	
		doc = open(line, "r")
		doc_list.append(Document(doc.read(), doc))
	return {h : doc_list}