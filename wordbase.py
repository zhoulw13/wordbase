import sys
import pickle
import codecs
import re
import time

def test():
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
	file_object.close()
	length = len(full_text)
	dictionary = {}
	position = 0
	i = 0
	wordS = False
	for c in full_text:
		if not c.isalpha():
			if wordS:
				wordS = False
				position+=1
				if word not in dictionary:
					dictionary[word] = []
				dictionary[word].append(position)
			continue
		else:
			if not wordS:
				wordS = True
				word = ''
				word = c.lower()
			else:
				word+=c.lower()

	output = open('dict.pkl', 'wb')
	pickle.dump(dictionary, output)
	output.close()

t0 = time.clock()
test()
print ("base time:%s\n" % (time.clock() - t0))