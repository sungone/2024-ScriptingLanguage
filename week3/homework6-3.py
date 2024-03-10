def reverse(number) :
    return int(str(number)[::-1])

def isPalindrome(number) :
    if(reverse(number) == number) :
        return True
    else :
        return False

def main() :
    num = input("정수 입력 : ")
    
    if isPalindrome(int(num)) == True :
        print("대칭수")
    else :
        print("대칭수 x")

if __name__ == "__main__" :
    main()
