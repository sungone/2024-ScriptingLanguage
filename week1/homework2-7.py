def conversion_year(minute) :
    return minute // (60 * 24 * 365)

def conversion_day(minute) :
    minute -= conversion_year(minute) * 365 * 24 * 60
    return minute // (60 * 24)

def main() :
    minute = input("분에 대한 숫자를 입력하세요 : ")
    print(int(minute) , "분은 약" , conversion_year(int(minute)) , "년" , conversion_day(int(minute)) , "입니다")

if __name__ == "__main__" :
    main()
