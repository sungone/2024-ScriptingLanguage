def triangle_width(x1 , y1 , x2 , y2 , x3 , y3) :
    edge1 = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5
    edge2 = ((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2)) ** 0.5
    edge3 = ((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1)) ** 0.5

    s = (edge1 + edge2 + edge3) / 2

    edge_1 = s - edge1
    edge_2 = s - edge2
    edge_3 = s - edge3

    return (s * edge_1 * edge_2 * edge_3) ** 0.5

def main() :
    x1 , y1 = input("x1 , y1 입력").split()
    x2 , y2 = input("x2 , y2 입력").split()
    x3 , y3 = input("x3 , y3 입력").split()

    print("넓이 : " , triangle_width(float(x1) , float(y1) , float(x2) , float(y2) , float(x3) , float(y3)))

if __name__ == "__main__" :
    main()