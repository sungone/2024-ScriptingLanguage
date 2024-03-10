def rating(num) :
    sum = 0
    for i in range(1 , num + 1 , 1) :
        sum += i / (i + 1)
    return sum

def test() :
    print("i\t\tm(i)")
    for i in range(1 , 21 , 1) :
        print(f"{i}\t\t{rating(i)}")

def main() :
    test()

if __name__ == "__main__" :
    main()
