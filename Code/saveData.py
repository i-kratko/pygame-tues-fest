import json

def saveData(dataFile, data):
    with open(dataFile, 'w') as f:
        json.dump(data, f)
    
def loadData(dataFile):
    with open(dataFile) as f:
        savedData = json.load(f)
    return savedData