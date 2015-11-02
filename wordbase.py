import sys
import pickle
import codecs
import re

def buildWordTree():
	if len(sys.argv) < 2:
		print ('Please input file name')
		return
	try:
		file_object = codecs.open(sys.argv[1], 'r', 'utf-8');
	except IOError:
		print ("file doesn't exsist")
		return
	full_text = ""
	full_text = file_object.read()
	length = len(full_text)
	dictionary = {}
	position = 1
	i = 0
	while i < length:
		word = ''
		while i < length and not full_text[i].isalpha():
			i+=1
		while i < length and full_text[i].isalpha():
			word+=full_text[i].lower()
			i+=1
		i+=1
		if word in dictionary:
			dictionary[word]+= ','+str(position)
		else:
			dictionary[word] = str(position)


	output = open('dict.pkl', 'wb')
	pickle.dump(dictionary, output)
	output.close()
	

if __name__ == "__main__":
	from timeit import Timer
	t = Timer('buildWordTree()', 'from __main__ import buildWordTree')
	print ('Runtime: ' + str(t.timeit(1)) + ' s')