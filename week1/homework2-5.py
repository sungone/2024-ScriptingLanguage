def get_tipMoney(money , tip) :
    return money * tip / 100

def main() :
    print("소계와 팁 비율을 입력하세요")
    my_money = input()
    my_tip = input()
    tip_amount = get_tipMoney(float(my_money), int(my_tip))
    total_amount = float(my_money) + tip_amount
    print("팁은" , tip_amount , "이고" , "총액은" ,  total_amount , "입니다.")
   

if __name__ == "__main__" :
    main()
