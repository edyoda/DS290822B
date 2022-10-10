# Abstraction
# means showing the funtionality and hiding the implementation

# abstract class - a class with atleast one abstract method
# abstract method - method with no body

from abc import ABC,abstractmethod

class laptop(ABC):               # abstract class
    @abstractmethod
    def processor(self):         # abstract method
        pass

    def keyboard(self):
        print("Keyword")

class programmer(laptop):
    def processor(self):
        print("Processor")

obj = programmer()
obj.processor()
obj.keyboard()
