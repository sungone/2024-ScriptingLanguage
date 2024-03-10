def gcd(m , n) :
    if m % n == 0 :
        print(f"{n}")
    else :
        gcd(n , m % n)

def main() :
    m , n = input("두 정수 입력").split()
    gcd(int(m) , int(n))
if __name__ == "__main__" :
    main()


