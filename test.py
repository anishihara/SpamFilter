import classifier
import training_data
import os

def extractText(filepath):
	file = open(filepath,"r")
	text = file.read()
	lines = text.split("\n")
	return "\n".join(lines[lines.index("")+1:])

def test(dirName,classificador,trainingData):
	easy_ham = os.listdir(dirName)
	if "cmds" in easy_ham : 
		easy_ham.remove("cmds")
	spamCount = 0;
	hamCount = 0;
	for file in easy_ham:
		text = extractText(dirName+"/"+file)
		spamProb = classificador.classify(text,trainingData.spam)
		hamProb = classificador.classify(text,trainingData.ham)
		if spamProb>hamProb: 
			spamCount += 1
		else: 
			hamCount += 1
	print dirName
	print "SPAM:",spamCount," HAM:",hamCount	

classificador = classifier.Classifier()
trainingData = training_data.TrainingData()
test("easy_ham",classificador,trainingData)
test("easy_ham_2",classificador,trainingData)
test("hard_ham",classificador,trainingData)
test("hard_ham_2",classificador,trainingData)
test("spam",classificador,trainingData)
test("spam_2",classificador,trainingData)

	
	
	
