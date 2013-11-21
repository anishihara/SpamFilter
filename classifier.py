import training_data
import re
import math

class Classifier:
	def classify(self,text,prior=0.5,c=10e-6):
		""" Remove a pontuacao do texto """
		words =  re.findall(r"[\w']+",text)
		"""words = text.split()"""
		data = training_data.TrainingData()
		spamLikehood = math.log(1)
		hamLikehood = math.log(1)
		for word in words:
			""" Calculo de spam"""
			if word in data.spam:
				spamLikehood += math.log(data.spam[word])
			else:
				spamLikehood += math.log(c)
			""" Calculo de ham"""
			if word in data.ham:
				hamLikehood += math.log(data.ham[word])
			else:
				hamLikehood += math.log(c)
		isSpam = spamLikehood + math.log(prior)
		isHam = hamLikehood +  math.log(prior)
		print "HAM:", isHam, "SPAM:", isSpam