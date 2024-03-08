def main() :
    name = input("사원 이름을 입력하세요 : ")
    week_worktime = input("주 당 근무시간을 입력하세요 : ")
    hour_pay = input("시간 당 급여를 입력하세요 : ")
    tax = input("원천징수세율을 입력하세요 : ")
    tax2 = input("지방세율을 입력하세요 :")
    money = int(week_worktime) * int(hour_pay)

    tax_1 = money * float(tax)
    tax_2 = money * float(tax2) 
    total_tax = tax_1 + tax_2

    print("사원 이름 : " , name)
    print("주당 근무시간 : " , int(week_worktime))
    print("임금 : " , int(hour_pay))
    print("총 급여 : " , money)
    print(f"공제\n 원천징수세(20.0 % ) : {int(tax_1)} \n주민세(9.0%) : {int(tax_2)} \n총 공제 : {int(total_tax)} \n공제 후 급여 : {int(money - total_tax)}")
    

if __name__ == "__main__" :
    main()