def bool_realroot(a , b , c) :
    if (b * b) - 4 * a * c > 0 :
        return 2
    elif (b * b) - 4 * a * c < 0 :
        return 0
    else :
        return 1

def realroot(a , b , c) :
    if bool_realroot(a , b , c) == 0 :
        print("이 방정식은 실근이 존재하지 않습니다.")
        return
    elif bool_realroot(a , b , c) == 1 :
        r = (-b + (((b * b) - (4 * a * c)) ** 0.5)) / (2 * a)
        print(f"실근은 : {r} 입니다")
        return
    elif bool_realroot(a , b , c) == 2 :
        r1 = (-b + (((b * b) - (4 * a * c)) ** 0.5)) / (2 * a)
        r2 = (-b - (((b * b) - (4 * a * c)) ** 0.5)) / (2 * a)
        print(f"실근은 {r1} 과 {r2} 입니다.")
        return
    
def main() :
    a , b , c = input("A , b , c 를 입력하세요").split()
    realroot(float(a) , float(b) , float(c))

if __name__ == "__main__" :
    main()