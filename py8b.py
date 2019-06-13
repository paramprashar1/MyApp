class Counter:

    ccount = 1

    def __init__(self):
        self.count = 1
        Counter.ccount = 1

    def incrementCount(self):
        self.count = self.count + 1
        Counter.ccount = Counter.ccount + 1

    def showCount(self):
        print("count is {} and ccount is {}".format(self.count, Counter.ccount))

c1 = Counter()
c2 = Counter()
c3 = c1

c1.incrementCount()
c2.incrementCount()
c3.incrementCount()

c1.incrementCount()
c2.incrementCount()
c3.incrementCount()

c4 = Counter()

c1.showCount()
c3.showCount()
c2.showCount()
c4.showCount()  