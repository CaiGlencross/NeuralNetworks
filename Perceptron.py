import time
import math
'''sampleList is a Vector where each element itself is a pair of the form:
		(inputVector, targetValue)'''
def Perceptron(sampleList, normal):
	weightVector = []
	startTime = time.time()
	'''add an extra 1 for learning threshold value'''
	weightVector.append(1)

	'''initialize weight vector to all 1's depending on input size'''
	for a in sampleList[0][0]:
		weightVector.append(0)


	print 'initial weight vector: ' + str(weightVector)

	'''append a 1 so we can learn the threshold value'''
	i=0
	print("initial input pairs")
	for inputPair in sampleList:
		if normal:
			inputPair[0] = normalize(inputPair[0])
		inputPair[0].insert(0,1)
		print "\tinputPair: " + str(inputPair) 


	perfectRecord = False

	'''repeat until we've gone through the whole sample list without fail''' 
	while perfectRecord == False:
		perfectRecord = True
		for inputPair in sampleList:
			zValue = 0
			print "inputPair: " + str(inputPair)
			print "weightVector: "+ str(weightVector)
			for i in xrange(0, len(inputPair[0])):
				zValue += weightVector[i] * inputPair[0][i]
			print "\tz value = " + str(zValue)
			print "\tthreshold = " + str(0)
			if zValue > 0:
				predictedValue = 1
			else:
				predictedValue = 0
			print "\tpredictedValue = " + str(predictedValue)
			targetValue = inputPair[1]
			print "\ttargetValue = " + str(targetValue)
			error = targetValue - predictedValue
			print "\terror: " + str(error)
			if error != 0:
				perfectRecord = False
			changeInWeights = map(lambda x: x * error, inputPair[0])
			#changeInWeights = error * weightVector
			print "\tchangeInWeights: " + str(changeInWeights)
			weightVector = sumArrays(changeInWeights, weightVector)
			print "\tnew weight vector = " + str(weightVector)


	print("runtime is %s seconds ---" % (time.time() - startTime))
	print(weightVector)

'''helper function for summing lists'''
def sumArrays(arrayA, arrayB):
	sumVector = []
	for i in xrange(0,len(arrayA)):
		sumVector.append(arrayA[i]+arrayB[i])
	return sumVector

def normalize(array):
	normalizedArray = []
	arraySum = 0
	for a in array:
		arraySum += (a**2)
	eDist = math.sqrt(arraySum)
	if eDist == 0:
		eDist = 1

	for i in xrange(0, len(array)):
		normalizedArray.append(float(array[i])/eDist)

	return normalizedArray
		



#implies function
#Perceptron( [[[0, 0], 1], [[0, 1], 1], [[1, 0], 0], [[1, 1], 1]], False )		

#nand function
#Perceptron([[[0, 0], 1], [[0, 1], 1], [[1, 0], 1], [[1, 1], 0]], False)

#iff function
#Perceptron([[[0, 0], 1], [[0, 1], 0], [[1, 0], 0], [[1, 1], 1]], False)

#majority function
# Perceptron([[[0, 0, 0], 0], [[0, 0, 1], 0], [[0, 1, 0], 0],
#                     [[1, 0, 0], 0], [[0, 1, 1], 1], [[1, 0, 1], 1],
#                       [[1, 1, 0], 1], [[1, 1, 1], 1]], False)

#modified & scaled nand
#Perceptron([[[0, 0], 1], [[0, 1], 1], [[1, 0], 1], [[100, 100], 0]], False)

#print normalize([1,2,3])

#nand modified and normalized
Perceptron([[[0, 0], 1], [[0, 1], 1], [[1, 0], 1], [[100, 100], 0]], True)



		
