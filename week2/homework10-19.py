from random import *

def game(ball , slot) :
    slots = []
    for i in range(slot) :
        slots.append(0) 
    
    rows = 5
    cols = slot - 1
    path = [[0 for j in range(cols)] for i in range(rows)]

    # 경로 만듬
    for i in range(rows) :
        for j in range(cols) :
            if(randint(1 , 2) == 1) :
                 path[i][j] = 'L'
            else :
                path[i][j] = 'R'

    # 슬롯에 모든 공 넣음
    for b in range(ball) :
        path_rand = randint(0 , 4)
        count = 0
        for i in range(cols) :
            if (path[path_rand][i] == 'R') :
                 count += 1

        slots[count] += 1
        
    # 출력
    for i in range(rows) :
        for j in range(cols) :
            print(path[i][j] , end='')
        print('')
       
    check_1 = True
    while (check_1) :
        check_1 = False
        for s in range(slot) :
            if(slots[s] != 0) :
                for i in range(s - 1) :
                    print(" " , end = '')
                print("o")
                slots[s] -= 1
                check_1 = True
       




def main() :
    ball_count = input("떨어뜨릴 공의 개수를 입력하세요 : ")
    slot_count = input("콩 기계의 슬롯 개수를 입력하세요 : ")

    game(int(ball_count) , int(slot_count))

if __name__ == "__main__" :
    main()