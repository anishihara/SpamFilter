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

import classifier
import training_data
import os
import email

def extract_body(payload):
    if isinstance(payload,str):
        return payload
    else:
        return '\n'.join([extract_body(part.get_payload()) for part in payload])

def extractText(filepath):
	file = open(filepath,"r")
	msgText = file.read()
	msg = email.message_from_string(msgText)
	payload = msg.get_payload()
	return extract_body(payload)
			
	"""
	lines = text.split("\n")
	return "\n".join(lines[lines.index("")+1:])
	"""
def test(dirName,classificador,trainingData):
	files = os.listdir(dirName)
	if "cmds" in files : 
		files.remove("cmds")
	"""Remover .DS_Store (arquivo gerado do Mac Os X) """
	if ".DS_Store" in files:
		files.remove(".DS_Store")
	#files = files[:1]
	spamCount = 0;
	hamCount = 0;
	for file in files:
		text = extractText(dirName+"/"+file)
		spamProb = classificador.classify(text,trainingData.spam,prior=0.2)
		hamProb = classificador.classify(text,trainingData.ham,prior=0.8)
		if spamProb>hamProb: 
			spamCount += 1
		else: 
			hamCount += 1
	totalCount = spamCount+hamCount
	print dirName
	print "SPAM:",float(spamCount)/float(totalCount)*100.0," HAM:",float(hamCount)/float(totalCount)*100.0

classificador = classifier.Classifier()
trainingData = training_data.TrainingData()
test("easy_ham_2",classificador,trainingData)
test("hard_ham",classificador,trainingData)
test("hard_ham_2",classificador,trainingData)
test("spam_2",classificador,trainingData)

	
	
	
