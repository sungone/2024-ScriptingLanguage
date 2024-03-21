class Stock :
    __symbol : str
    __name : str
    __previousClosingPrice : float
    __currentPrice : float

    def __init__(self , symbol , name , previousClosingPrice , currentPrice) :
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getName(self) :
        return self.__name
    
    def getSymbol(self) :
        return self.__symbol
    
    def setPreviousClosingPrice(self , price) :
        self.__previousClosingPrice = price
    
    def getPreviousClosingPrice(self) :
        return self.__previousClosingPrice
    
    def setCurrentPrice(self , price) :
        self.__currentPrice = price
    
    def getCurrentPrice(self) :
        return self.__currentPrice
    
    def getChangePercent(self) :
        return (self.__currentPrice - self.__previousClosingPrice) / self.__previousClosingPrice
    
def main() :
    t = Stock('INTC' , 'Intel Corporation' , 20500 , 20350)
    t_rate = t.getChangePercent()
    print("가격 변동률 : " , (t_rate * 100) , '%')

if __name__ == "__main__" :
    main()


        