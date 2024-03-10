def determine_dot(x , y) :
    if x > 0 and x < 200 :
        if (-(0.5 * x) + 100) > y and y > 0 :
            print("점은 삼각형의 내부에 있습니다.")
            return

    print("점은 삼각형의 내부에 있지 않습니다.")

def main() :
    x , y = input("점의 x 와 y 좌표값을 입력하세요 : ").split()
    determine_dot(float(x) , float(y))

if __name__ == "__main__" :
    main()
