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


class TrainingData:
	def __init__(self,spamTrainingDataFilePath = "spam_df.csv",hamTrainingDataFilePath = "easyham_df.csv"):
		self.spam = self.getTrainingData(spamTrainingDataFilePath)
		self.ham = self.getTrainingData(hamTrainingDataFilePath)
		
	"""
	Retorna um dicionario dado um filepath de arquivo csv dos dados de treino.
	"""
	def getTrainingData(self,filepath):
		filetext = open(filepath,"r")
		result = {}
		ignore = True
		for line in (raw.strip().split() for raw in filetext):
			if ignore:
				ignore = False
			else:
				columns = line[0].split(',')
				result[columns[0].strip('"')] = float(columns[3])
		return result