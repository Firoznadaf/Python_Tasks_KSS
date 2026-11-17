#  Shape Area Calculator (Polymorphism) 

import math

class Circle:
    def area(self):
        r = 5
        print("Circle Area:", math.pi * r * r)

class Reactangle:
    def area(self):
        l = 10
        w = 5
        print("Reactangle Area:", l * w)

class Triangle:
    def area(self):
        b= 10
        h = 5
        print("Triangle Area", 0.5 * b * h)

shapes = [Circle(), Reactangle(), Triangle()]

for shape in shapes:
    shape.area()