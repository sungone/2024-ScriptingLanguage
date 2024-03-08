def getRightmostLowestPoint(points : list) :
    
    most_right = points[0][0]
    most_right_list = []
    most_down = points[0][1]
    most_down_list = []
    for i in range(6) :
        if most_right <= points[i][0] :
            if most_right == points[i][0] :
                if most_down > points[i][1] :    
                    most_right < points[i][0]
                    most_right_list = points[i]
            else :
                most_right < points[i][0]
                most_right_list = points[i]
        if most_down >= points[i][1] :
            if most_down == points[i][1] :
                if most_right < points[i][0] :    
                    most_down = points[i][1]
                    most_down_list = points[i]
            else :
                most_down = points[i][1]
                most_down_list = points[i]
    
    if abs(float(most_down_list[0])) + abs(float(most_down_list[1])) > abs(float(most_right_list[0])) + abs(float(most_right_list[1])) :
        return most_down_list
    else :
        return most_right_list
    
def main() :
    point_list = [[0 for j in range(2)] for i in range(6)]
    print("6개의 점을 입력하세요")
    for i in point_list :
        i[0] ,i[1] = input().split()

    result = getRightmostLowestPoint(point_list)
    print(f"최우측하단의 점은 : {result} 입니다.")


if __name__ == "__main__" :
    main()