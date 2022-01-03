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
        "create the first serial number with a start number"
        self.start=start
        self.next=self.start
    def __repr__(self):
        rep = f"SerialGenerator start={self.start},next= {self.next}"
        return rep
    def generate(self):
        "return the next sequential number"
        self.next=self.next+1
        return self.next-1
    def reset(self):
        "reset the number back to the original start number"
        self.next=self.start

