import random

class Allele:
    # Class of list of alleles

    def __init__(self):
        # initiate the object with a random list
        self._lst = Allele.randomList()
        # A list consists of A and a
        self._letters = ""
        # frequency of A, default 50%
        self._freq = 5
        # If it is fixated
        self._isFixated = False
        # number of generations
        self._generations = 1

    # Perform a cross, update frequency and allele
    # Update the list of Aa
    def cross(self):
        freq = 0
        alleleLst = []
        for i in range(len(self._lst)):
            if self._lst[i] < self._freq:
                freq += 1
                alleleLst.append("A")
            else:
                alleleLst.append("a")
        # Check if it is fixated
        if freq == 0 or freq == 10:
            self._isFixated = True
        self._letters = " ".join(alleleLst)
        self._freq = freq
        self._lst = Allele.randomList()
        self._generations += 1

    # Static methods
    # Generate a random number from 0-9
    def randomList():
        lst = []
        for i in range(10):
            lst.append(random.randrange(0,10))
        return lst

if __name__ == '__main__':
    a1 = Allele()
    while not a1._isFixated:
        print(a1._lst, "  ", a1._freq)
        a1.cross()
        print(a1._letters)
    print("Result: ", a1._freq)
    print("Generations: ", a1._generations)
