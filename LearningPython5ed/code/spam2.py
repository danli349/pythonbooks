def printNumInstances():
    print("Number of instances created: %s" % Spam.numInstances)

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1
