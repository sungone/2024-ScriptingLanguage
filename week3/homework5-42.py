import random

def random_dot() :
    x = random.random()
    if(random.randint(0 , 1) == 0) :
        x = -x
    y = random.random()
    if(random.randint(0 , 1) == 0) :
        y = -y

    if x < 0 :
        return 1
    if x > 0 and y > 0 and (-x + 1) > y :
        return 1
    return 0
def main() :

    odd_nums = 0
    for i in range(1000000) :
        odd_nums += int(random_dot())

    print(f"홀수번호의 공간에 다트가 맞은 개수 : {odd_nums}")
    
if __name__ == "__main__" :
    main()
