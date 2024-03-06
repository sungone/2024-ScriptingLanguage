def whatMile(killometer , minutetimetime) :
    mykillo = (killometer * 60) / minutetimetime
    return mykillo / 1.6

def main() :
    print("시속 몇 마일: " , whatMile(14 , 45.5))

if __name__ == "__main__" :
    main()
