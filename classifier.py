"""
Copyright (C) 2013 by Anderson Nishihara

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

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
		punctuationRegex = "["+ string.punctuation + "\t\s]"
		words = re.split(punctuationRegex ,text.lower())
		# Remove stop words em ingles
		words = [w for w in words if not w in self.stopwords]
		words = Counter(words)
		likehood = 0.0
		for word, ocurrence in words.items():
			# Nao calcula nada para termos que aparecem apenas uma vez no texto e menores que 3 letras
			if ocurrence > 1 and len (word)>2:
				# Calculo do likehood em escala de log
				if word in trainingData:
					likehood += math.log(trainingData[word])*ocurrence
				else:
					likehood += math.log(c)*ocurrence
		return likehood + math.log(prior)