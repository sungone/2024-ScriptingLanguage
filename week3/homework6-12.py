def printChars(ch1 , ch2 , numberPerLine) :

   for ch in range(ord(ch1) , ord(ch2) , numberPerLine) :
        count = 0
        while(count < numberPerLine) :
            print(chr(ch + count) , end='')
            count += 1
            if(ch + count - 1 == ord(ch2)) :
                break 
        print("")

def main() :
    printChars('1' , 'Z' , 10)

if __name__ == "__main__" :
    main()
