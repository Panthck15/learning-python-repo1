class Circle:
    def __init__(self,radius):
        self.raduis=radius

    def circle_area(self):
        #print(22/7)
        self.area=(22/7)*(self.raduis**2)
        return self.area

r1 = Circle(4)
print(r1.circle_area())