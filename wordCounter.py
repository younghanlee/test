#!/usr/bin/python


def fileToList(filename):
    outputList = list()
    file = open(filename, 'r')
    for line in file:
        if not line.strip().startswith("#"):
            outputList.append(line.strip())
    file.close()
    return outputList


def listToWord(inputList):
    outputList = list()
    for line in inputList:
        words = line.split()
        for word in words:
            outputList.append(word)
    return outputList
    
    
def wordCounter(inputList):
    outputDict = dict()
    for word in inputList:
        outputDict[word] = outputDict.get(word, 0) + 1
    return outputDict


def mergeWordCounter(totalDict, inputDict):
    for key in inputDict:
        totalDict[key] = totalDict.get(key, 0) + inputDict[key]
    return totalDict
    
    
def getProbability(inputDict):
    outputDict = dict()
    totalCounter = 0.0
    for key in inputDict:
        totalCounter += inputDict[key]
    for key in inputDict:
        outputDict[key] = inputDict[key] / totalCounter
    return outputDict
    
    
def getFileList(filename):
    return fileToList(filename)
    
    
def main():
    lineList = fileToList("sample.txt")
    wordList = listToWord(lineList)
    wordDict = wordCounter(wordList)

    lineList1 = fileToList("sample1.txt")
    wordList1 = listToWord(lineList1)
    wordDict1 = wordCounter(wordList1)

    mergeWordCounter(wordDict, wordDict1)

    print getProbability(wordDict)
    
    
if __name__ == "__main__":
    main()