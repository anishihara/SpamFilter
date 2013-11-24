import re
import math
from collections import Counter
import string

class Classifier:
	def __init__(self):
		stopwordsFile = open("common-english-words.txt","r")
		self.stopwords = stopwordsFile.read().split(',')
	
	def classify(self,text,trainingData,prior=0.5,c=10e-6):
		# Remove numeros
		text = re.sub("[0123456789]", "", text)
		# Remove a pontuacao do texto
		words = re.split("["+ string.punctuation + "\t\s]" ,text.lower())
		# Remove stop words em ingles
		words = [w for w in words if not w in self.stopwords]
		words = Counter(words)
		likehood = 0.0
		for word, ocurrence in words.items():
			# Nao calcula nada para termos que aparecem apenas uma vez no texto e menores que 3 letras
			if ocurrence > 1 and len (word)>2:
				# Calculo do likehood em escala de log
				if word in trainingData:
					likehood += math.log(trainingData[word])
				else:
					likehood += math.log(c)
		return likehood + math.log(prior)