from nltk import word_tokenize
from nltk.stem import *
import nltk.data
from math import log

class Summarizer:

	def __init__(self):
		self.infile = ''
		self.outfile = ''
		self.numsentences = 1
		self.wordFrequencies = {}
		self.finalWordFrequencies = {}
		self.sentenceFrequencies = {}
		self.totalWords = 0

	def computeSentences(self,text):
		sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
		generatedSentences = sent_detector.tokenize(text)
		return generatedSentences
		

	def summarize(self, infile, outfile, numsentences):
		self.infile = infile
		self.outfile = outfile
		self.numsentences = numsentences


		f = open(self.infile)

		text = f.read().decode('utf-8')

		tokens = word_tokenize(text)

		stemmer = PorterStemmer()

		for token in tokens:
			token = stemmer.stem(token)
			
			if token in self.wordFrequencies:
				# Have seen this token already
				self.wordFrequencies[token]+=1
			else:
				# Havent seen this toekn yet
				self.totalWords+=1
				self.wordFrequencies[token] = 1

		for token in tokens:
			token = stemmer.stem(token)
			self.finalWordFrequencies[token] = (log(float(self.wordFrequencies[token])/float(self.totalWords)))

		sentences = self.computeSentences(text)
		
		for sent in sentences:
			self.sentenceFrequencies[sent] = 0

			tokens = word_tokenize(sent)

			stemmer = PorterStemmer()

			for token in tokens:
				token = stemmer.stem(token)
				self.sentenceFrequencies[sent]+=self.finalWordFrequencies[token]

		print self.sentenceFrequencies













if __name__ == '__main__':
	mySummarizer = Summarizer()
	mySummarizer.summarize('infile.txt','outfile.txt',4)











