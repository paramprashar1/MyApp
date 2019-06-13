class Counter:

    def __init__(self):
        self.count=1

    def incrementCount(self):
        self.count +=1

    def showCount(self):
        print("Count is {}".format(self.count))