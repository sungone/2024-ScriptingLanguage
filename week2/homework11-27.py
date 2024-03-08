def sortColumns(m : list) :
    new_m = [[0 for j in range(3)] for i in range(3)]
    
    for i in range(3) :
        for j in range(3) :
            new_m[i][j] = m[j][i]

    for i in range(3) :
        new_m[i].sort() 

    for i in range(3) :
        for j in range(3) :
            m[j][i] = new_m[i][j]

    return m

def main() :
    arr = [[0 for j in range(3)] for i in range(3)]
    new_arr = [[0 for j in range(3)] for i in range(3)]
    print("3X3 행렬을 한 행씩 입력하세요 : ")
    for i in range(3) :
        arr[i][0] , arr[i][1] , arr[i][2] = input().split()

    new_arr = sortColumns(arr)

    print("열 정렬된 리스트는 다음과 같습니다.")
    for i in range(3) :
            print(new_arr[i])
if __name__ == "__main__" :
    main()