def many_num(nums : list) :
    nums_dict = {}
    for i in nums :
        if(i in nums_dict) :
            nums_dict[i] += 1
        else :
            nums_dict[i] = 1

    what_most_key = [nums[0]]
    what_most_value = nums_dict[nums[0]]
    for key , value in nums_dict.items() :
        if(what_most_value == value and key not in what_most_key) :
            what_most_key.append(key)
        elif(what_most_value < value) :
            what_most_value = value
            what_most_key.clear()
            what_most_key.append(key)
        

    return what_most_key

def main() :
    nums = [int(x) for x in input("정수 입력 : ").split()]
    print("가장 많이 나온 수 : " , str(many_num(nums)))

if __name__ == "__main__" :
    main()