import sys
from matplotlib.pyplot import specgram
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import cPickle
import scipy

values = dict()

# order: classical, country, jazz, pop, rock, metal

def input():

	
	indVal = 0
	fftArray = []
	outputName = "pickledValues"
	for index,arg in enumerate(sys.argv[1:]):
		index+=1
		sample_rate, x = wav.read(arg)
		fftFea = abs(scipy.fft(x)[:1000])
		
		values[index] = fftFea

		# fftArray.append(fftFea)
		# if (index % 100) == 99:
		# 	values[indVal] = fftArray
		# 	indVal+=1
		# 	fftArray = []
	
	f = open(outputName,"wb")
	cPickle.dump(values,f,protocol=2)
	f.close()

	# print values

if __name__ == '__main__':
	input()