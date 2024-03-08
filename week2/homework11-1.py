def sumColumn(m : list, columnIndex : int) :
    
    sum_list = [0 , 0 , 0 , 0]
    for i in range(3) :
        for j in range(columnIndex) :
            sum_list[j] +=  float(m[i][j]) 

    return sum_list

def main() :
    arr = [[0 for j in range(4)] for i in range(3)]
   
    for i in range(3) :
        arr[i][0] , arr[i][1] , arr[i][2] , arr[i][3] = input(f"3X4 행렬의 행 {i} 번에 대한 원소를 입력하세요").split()

    final_list = sumColumn(arr , 4)
       
    for i in range(4) :
        print(f"열 {i} 번 원소의 총 합은 {final_list[i]} 입니다.")

if __name__ == "__main__" :
    main()