def add_digit(num) :
    sum = 0
    digit = (num % 10)
    for i in range(digit , -1 , -1) :
        set_num =  num // pow(10 , i) 
        sum += set_num
        num -= set_num * pow(10 , i)   
    return sum

def main() :
    a = input("0과 1000 사이의 숫자를 입력하세요 : ")
    print("이 자릿수들의 합은 " , add_digit(int(a)) , "입니다")

if __name__ == "__main__" :
    main()