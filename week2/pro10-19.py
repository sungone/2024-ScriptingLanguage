import random

nOfBalls = eval(input('공의 개수 : '))
nOfSlots = eval(input('슬롯의 개수 : '))

slots = [0] * nOfSlots ## 슬롯의 개수만큼 0으로 초기화

### 슬롯 출력 #######
for i in range(nOfBalls) : ## 공의 개수만큼 반복
    count = 0 ## R의 개수를 센다
    for j in range(nOfSlots - 1) : ## 슬롯 - 1 번 만큼 반복
        if random.random() > 0.5 :
            print('R' , end='') ## 강제로 한줄 띄는 것을 방지
            count += 1
        else :
            print('L' , end='')
    print()
    slots[count] += 1 ## 해당 슬롯에 공 한개 추가


### 공 출력 #######
Max = max(slots) ## 최댓값
for h in range(Max , 0 , -1) : ## h = Max , Max - 1 ...  , 1
    for i in slots :
        if i >= h :
            print('o' , end='')
        else :
            print(' ', end='')
    print()





