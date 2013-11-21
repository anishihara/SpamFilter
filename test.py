import classifier
import os

def extractText(filepath):
	file = open(filepath,"r")
	text = file.read()
	lines = text.split("\n")
	return "\n".join(lines[lines.index("")+1:])
		

classificador = classifier.Classifier()
easy_ham = os.listdir("easy_ham")
if "cmds" in easy_ham : 
	easy_ham.remove("cmds")
easy_ham = easy_ham[1:2]
for file in easy_ham:
	text = extractText("easy_ham/"+file)
	classificador.classify("what text can I test")
	
	
