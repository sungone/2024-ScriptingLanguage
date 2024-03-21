class GeometricObject :
    def __init__(self , color = "blue", filled = True) :
        self.color = color
        self.filled = filled

class Triangle(GeometricObject) :
    def __init__(self , side1 = 1 , side2 = 2, side3 = 3) :
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getArea(self) :
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def getPerimeter(self) :
        return self.side1 + self.side2 + self.side3
    
    def __str__(self) :
        return "Triangle : side1 = " + str(self.side1) + "side2 = " + str(self.side2) + "side3 = " + str(self.side3)
    
    def info(self) :
        print(f"color : {self.color} , filled : {self.filled} , area : {self.getArea()} , perimeter : {self.getPerimeter()}")
    
t = Triangle(10 , 20 , 30)
t.filled = True
t.color = "yellow"
t.info()
