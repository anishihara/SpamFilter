import re
import math

class Classifier:
	def classify(self,text,trainingData,prior=0.5,c=10e-6):
		""" Remove a pontuacao do texto """
		words =  re.findall(r"[\w']+",text)
		"""words = text.split()"""
		likehood = math.log(1)
		for word in words:
			""" Calculo do likehood """
			if word in trainingData:
				likehood += math.log(trainingData[word])
			else:
				likehood += math.log(c)
		return likehood + math.log(prior)