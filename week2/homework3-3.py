import math
import numpy as np

def greatcircle_distance(x1 , y1 , x2 , y2) :
    r = 6370.01
    sin_num = math.sin(math.radians(x1)) * math.sin(math.radians(x2))
    cos_num = math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos(math.radians(y1) - math.radians(y2))
    d = r * np.arccos(sin_num + cos_num)
    return d

def triangle_width(d1 , d2 , d3) :
    s = (d1 + d2 + d3) / 2

    d_1 = s - d1
    d_2 = s - d2
    d_3 = s - d3

    return (s * d_1 * d_2 * d_3) ** 0.5

def main() :
    Gwangju_x , Gwangju_y = 35.1768201 , 126.7735892
    Busan_x , Busan_y = 35.1645701 , 129.0015892
    Gangneung_x , Gangneung_y = 37.7637326 , 128.8824475
    Seoul_x , Seoul_y = 37.565289 , 126.8491259

    Gwangju_to_Busan = greatcircle_distance(Gwangju_x , Gwangju_y , Busan_x , Busan_y)
    Busan_to_Gangneung = greatcircle_distance(Busan_x , Busan_y , Gangneung_x , Gangneung_y)
    Gangneung_to_Seoul = greatcircle_distance(Gangneung_x , Gangneung_y , Seoul_x , Seoul_y)
    Seoul_to_Gwangju = greatcircle_distance(Seoul_x , Seoul_y , Gwangju_x , Gwangju_y)
    Gangneung_to_Gwangju = greatcircle_distance(Gangneung_x , Gangneung_y , Gwangju_x , Gwangju_y)
    Seoul_to_Busan = greatcircle_distance(Seoul_x , Seoul_y , Busan_x , Busan_y)

    width1 = triangle_width(Gwangju_to_Busan , Busan_to_Gangneung , Gangneung_to_Gwangju)
    width2 = triangle_width(Gangneung_to_Seoul , Seoul_to_Gwangju , Seoul_to_Busan)

    print("네 도시에 둘러쌓인 넓이 : ", width1 + width2 , "km^2")

if __name__ == "__main__" :
    main()