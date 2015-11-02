import sys
import pickle
import codecs

def query():
	if len(sys.argv) < 2:
		print ('Please input query file name')
		return

	pkl_file = open('dict.pkl', 'rb')
	dictionary = pickle.load(pkl_file)
	pkl_file.close()

	try:
		query_file = codecs.open(sys.argv[1], 'rU', 'utf-8');
	except IOError:
		print ("file doesn't exsist")
		return

	try:
		for line in query_file.readlines():
			line=line.strip('\n')
			line=line.strip('\r')
			line=line.lower()
			print(dictionary[str(line)])
	finally:
		query_file.close()

if __name__ == '__main__':
	from timeit import Timer
	t = Timer('query()', 'from __main__ import query')
	print ('Runtime: ' + str(t.timeit(10)) + ' s')