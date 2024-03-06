def get_Area(width , height) :
    return width * height

def get_Round(width , height) :
    return 2 * (width + height)

def main() :
    print("넓이 :" , get_Area(4.5 , 7.9))
    print("둘레 :" , get_Round(4.5 , 7.9))

if __name__ == "__main__" :
    main()



