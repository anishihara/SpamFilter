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