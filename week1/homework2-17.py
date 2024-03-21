def main() :
    weight = input("몸무게를 파운드로 입력하세요 : ")
    stature = input("키를 인치로 입력하세요 : ")

    weight = float(weight) * 0.45359237
    stature = float(stature) * 0.0254

    BMI = weight / (stature ** 2)
    print("BMI 는" , BMI , "입니다.")

if __name__ == "__main__" :
    main()
