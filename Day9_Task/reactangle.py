#  Rectangle Area Calculator (Constructor) 

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of Reactangle:", self.length * self.width)

r = Rectangle(10, 5)
r.area()