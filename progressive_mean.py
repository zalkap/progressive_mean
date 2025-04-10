
class ProgressiveMean():

    def __init__(self):
        self._length = 0
        self._mean = 0
        self._next_value = 0

    @property  
    def mean(self):
        return self._mean

    @property
    def length(self):
        return self._length

    def add_next(self, value):
        self._length += 1
        self._mean = ((self.mean * (self.length - 1)) + value) / self.length
        return self.mean
