class Rectangle:
    def __init__(self,length, width):
        self.length=length
        self.width=width

    def rect_area(self):
        self.area=self.length*self.width
        return self.area

r1 = Rectangle(3,4)
print(r1.rect_area())

