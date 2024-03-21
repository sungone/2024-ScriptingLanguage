def main() :
    ta = input("화씨 -58F 와 41F 사이의 온도를 입력하세요 : ")
    v = input("풍속을 시간 당 마일 단위로 입력하세요 : ")

    ta = float(ta)
    v = float(v)
    
    twc = 35.74 + 0.6215 * ta - 35.75 * (v ** 0.16) + 0.4275 * ta * (v ** 0.16)

    print("체감온도는" , twc , "입니다.")

if __name__ == "__main__" :
    main()
