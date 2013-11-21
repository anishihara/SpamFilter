import training_data

class Classifier:
	def classify(self,text,prior=0.5,c=10e-6):
		words =  [splited.strip("\\'\".,:") for splited in text.split()]
		data = training_data.TrainingData()
		spamLikehood = 1
		hamLikehood = 1
		for word in words:
			""" Calculo de spam"""
			if word in data.spam:
				spamLikehood *= data.spam[word]
			else:
				spamLikehood *= c
			""" Calculo de ham"""
			if word in data.ham:
				hamLikehood *= data.ham[word]
			else:
				hamLikehood *= c
		isSpam = spamLikehood * prior
		isHam = hamLikehood * prior
		print "HAM:", isHam
		print "SPAM:", isSpam