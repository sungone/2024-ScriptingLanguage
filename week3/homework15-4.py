def recursion(i) :
    if i == 0 :
        return
    if i == 1 : 
        return 1
    else :
        return (recursion(i - 1) + (1 / i))

def main() :
    for i in range(11) :
        print(i , "\t" , recursion(i))
if __name__ == "__main__" :
    main()

