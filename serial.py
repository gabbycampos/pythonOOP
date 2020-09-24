"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        self.start = start

    def generate(self):
        ''' Return next number '''
        self.start += 1
        return self.start - 1

    def reset(self):
        ''' Reset number '''
        self.__init__()


# serial = SerialGenerator(start=100)
# print(serial.generate())
# print(serial.generate())
# # print(serial.generate())
# # print(serial.generate())
# # print(serial.generate())
# print(serial.reset())
# print(serial.generate())
# serial = SerialGenerator(start=50)
# print(serial.generate())
