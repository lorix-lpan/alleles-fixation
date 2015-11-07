import random

class Allele:
    # Class of list of alleles

    def __init__(self):
        # initiate the object with a random list
        self._lst = Allele.randomList()
        # frequency of A, default 50%
        self._freq = 5
        # If it is fixated
        self._isFixated = False
        # number of rounds
        self._rounds = 0

    # Perform a cross, update frequency and allele
    def cross(self):
        freq = 0
        for i in range(len(self._lst)):
            if self._lst[i] < self._freq:
                freq += 1
        # Check if it is fixated
        if freq == 0 or freq == 10:
            self._isFixated = True
        self._freq = freq
        self._lst = Allele.randomList()
        self._rounds += 1


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
    print("Result: ", a1._freq)
    print("Rounds: ", a1._rounds)
