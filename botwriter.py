import random
import string
import nltk
from nltk.corpus import stopwords
import re



def generate(model):
	start = random.randint(0, len(model))
	words= model.keys()
	word = words[start]
	sent = word + " "
	for i in range(100):
		words = model[word]
		word = words[random.randint(0, len(model[word])-1)]
		sent = sent + word + " "
	return sent

def generatebi(unimodel, bimodel):
	start = random.randint(0, len(unimodel))
	words = unimodel.keys()
	word1 = words[start]
	word2 = words[random.randint(0, len(unimodel))]
	sent = word1 + " " + word2 + " "

	for i in range(100):
		d1 = bimodel[word1]
		if word2 in d1:
			words = d1[word2]
		else:
			words = unimodel[word2]

		word = words[random.randint(0, len(words)-1)]
		
		sent = sent + word + " "
		word1 = word2
		word2 = word
	return sent

def trainuni(text):
	#split
	worddict = {}
	words = text.split(" ")
	filtered_words = filter(lambda token: token not in stopwords.words('english'), words)
	for i in range(len(words)-1):
		word = words[i]
		if not word in worddict:
			worddict[word] = [words[i+1]]
		else:
			worddict[word].append(words[i+1])

	return worddict

def trainbi(text):
	#split
	worddict = {}
	words = text.split(" ")
	#filtered_words = filter(lambda token: token not in stopwords.words('english'), words)
	
	for i in range(2, len(words)):
		word = words[i]
		
		fword = words[i-2]
		sword = words[i-1]
		
		if not fword in worddict:
			worddict[fword] = {}

		if not sword in worddict[fword]:
			worddict[fword][sword] = [word]
		else:
			worddict[fword][sword] = worddict[fword][sword] + [word] 



	return worddict


#file = open('big.txt', 'r')
file = open("sherlockHolmes.txt", 'r')
text = file.read()
file.close()
umodel = trainuni(text)
bmodel = trainbi(text)
print "trained"
for i in range(5):
	print generatebi(umodel, bmodel)





