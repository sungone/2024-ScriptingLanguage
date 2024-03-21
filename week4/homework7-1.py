class Rectangle :
    def __init__(self , width , height) :
        self.width = width
        self.height = height
    
    def getArea(self) :
        return self.width * self.height
    def getPerimeter(self) :
        return 2 * (self.width + self.height)
    
def main() :
    r1 = Rectangle(4 , 10)
    r2 = Rectangle(3.5 , 35.7)

    print("r1 의 폭 : " , r1.width , "r1 의 높이 : " , r1.height)
    print("r1 의 높이 : " , r1.getArea() , "r1 의 둘레 : " , r1.getPerimeter())
    

                   
if __name__ == "__main__" :
    main()



    