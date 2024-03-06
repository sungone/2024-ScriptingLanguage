def populationNum(current_year) :
    second = 365 * 24 * 60 * 60
    birth = second // 7
    death = second // 13
    comein = second // 45

    return 312032486 + (current_year * (birth - death + comein))

def main() :
    for i in range(5 , 50 , 5) :
        print(i , "년 후 인구: " , populationNum(i))

if __name__ == "__main__" :
    main()
