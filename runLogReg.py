import sys
import cPickle
import numpy as np
from random import shuffle


values = []
randList = []
randListSplit = []

def initial():
	values = loadPickle(sys.argv[1])
	randList = range(1,len(values)+1) # list of indicies 
	shuffle(randList)                 # of which are shuffled 
	
	# this split if for 10 fold cross validation
	randListSplit = [randList[i:i+60] for i in xrange(0,600,60)]

	

def loadPickle(file):
	# LOADS ALL D PICKLES
	print "Pickling..."
	f = open(file)
	v = cPickle.load(f)
	f.close()
	return v

if __name__ == '__main__':
	initial()