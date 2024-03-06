def conversion_pound_killo(pound) :
    killo = (227 * pound) / 500
    return killo

def main() :
    my_pound = input("파운드 값을 입력하세요 : ")
    print(my_pound , "파운드는" , conversion_pound_killo(float(my_pound)) , "킬로그램입니다.")

if __name__ == "__main__" :
    main()
