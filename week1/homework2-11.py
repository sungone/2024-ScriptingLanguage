def main() :
    total_money = input("약정 금액을 입력하세요 : ")
    rate = input("연이율(%)을 입력하세요 : ")
    year = input("약정 기간(년) 을 입력하세요 : ")

    total_money = int(total_money)
    rate = float(rate)
    year = int(year)

    month_money = total_money / ((1 + (rate / 100 / 12)) ** (year * 12))
    print("월 납입금은" , month_money , "입니다")

if __name__ == "__main__" :
    main()
