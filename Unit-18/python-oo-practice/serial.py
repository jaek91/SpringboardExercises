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

    def __init__(self,start):
        """constructor function to generate serial number from start"""
        self.value = start
        self.steps = 0 


    def generate(self):
        """Return the next serial number by incrementing 1 from the current value"""
        previous_value = self.value
        self.value += 1
        self.steps += 1
        return previous_value

    def reset(self):
        """resets the current serial number to the start value"""
        self.value = self.value - self.steps

