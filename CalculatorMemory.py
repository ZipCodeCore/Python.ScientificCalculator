

class MemoryFn:

    def __init__(self, calcVal):
        self.calcVal = calcVal


    def resetMem(self):
        self.calcVal = 0


    def getlastMemVal(self):
        return self.calcVal


    def setMemVal(self,displayedVal):
        self.calcVal = displayedVal



