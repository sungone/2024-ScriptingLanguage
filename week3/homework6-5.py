def displaySortedNumbers(num1 , num2 , num3) :
    my_list = [num1 , num2 , num3]
    my_list.sort()
    print(f"정렬된 숫자는 {my_list[0]} {my_list[1]} {my_list[2]} 입니다")

def main() :
    a , b , c = input("세 개의 수를 입력하세요 : ").split()
    displaySortedNumbers(float(a) , float(b) , float(c))

if __name__ == "__main__" :
    main()
