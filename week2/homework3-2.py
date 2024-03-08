import math
import numpy as np

def greatcircle_distance(x1 , y1 , x2 , y2) :
    r = 6370.01
    sin_num = math.sin(math.radians(x1)) * math.sin(math.radians(x2))
    cos_num = math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos(math.radians(y1) - math.radians(y2))
    d = r * np.arccos(sin_num + cos_num)
    return d


def main() :
    x1 , y1 = input("첫 번째 점(위도와 경도) 을 60분법 각으로 입력하세요 : ").split()
    x2 , y2 = input("두 번째 점(위도와 경도) 을 60분법 각으로 입력하세요 : ").split()

    print("두 점 사이의 거리는" , greatcircle_distance(float(x1) , float(y1) , float(x2) , float(y2)) ,"km 입니다.")

if __name__ == "__main__" :
    main()