import pickle

def dumpPickle(fileName, obj):
    with open(fileName, mode="wb") as f:
        pickle.dump(obj, f)
        
def loadPickle(fileName):
    with open(fileName, mode="rb") as f:
        return pickle.load(f)