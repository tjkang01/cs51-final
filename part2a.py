# 2a. Write a method that takes in a string and creates a new Document from a file with filename equal to the string.

def filename_to_doc(string):
# string is the string to be converted into a document 
	return Document(None, string)