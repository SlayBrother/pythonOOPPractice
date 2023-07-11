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

    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def generate(self):
        start_number = self.b
        self.b += 1
        return start_number

    def reset(self):
        self.b = self.a

serial = SerialGenerator(a=100,b=100)
print(serial.generate())  # Output: 100
print(serial.generate())  # Output: 101
print(serial.generate())  # Output: 102
serial.reset()
print(serial.generate())  # Output: 100