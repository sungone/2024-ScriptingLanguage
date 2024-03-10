from random import *

def Select_Card(num1 = int , num2 = int) :
    my_card = num1 + (num2 * 10)
    card_num = my_card // 10
    card_patton = my_card % 10

    if(card_patton == 1) :
        card_patton = '크로바'
    elif(card_patton == 2) :
        card_patton = '다이아몬드'
    elif(card_patton == 3) :
        card_patton = '하트'
    else :
        card_patton = '스페이드'

    if(card_num == 1) :
        card_num = 'A'
    elif(card_num == 11) :
        card_num = 'J'
    elif(card_num == 12) :
        card_num = 'Q'
    elif(card_num == 13) :
        card_num = 'K'

    print(f"당신이 뽑은 카드는 {card_patton} {card_num} 입니다.")

def main() :

    your_card1 = randint(1 , 4)
    your_card2 = randint(1 , 13)
    Select_Card(your_card1 , your_card2)

if __name__ == "__main__" :
    main()