'''
파이썬 과제04
커피 자판기 프로그램
'''
def printmenu() :
    print("---------------------------")
    print("\t\t커피자판기 (300원)")
    print("1. 블랙 커피")
    print("2. 프림 커피")
    print("3. 설탕 프림 커피")
    print("4. 재고 현황")
    print("5. 종료")

def blackcoffee() :
    global coffee
    global water
    global cup
    global money
    global coin
    coffee = coffee - 30
    water = water - 100
    cup -= 1
    money -= 300
    coin += 300
    

def frimcoffee() :
    global coffee
    global water
    global frim
    global cup
    global money
    global coin
    coffee = coffee - 15
    frim = frim - 15
    water = water - 100
    cup -= 1
    money -= 300
    coin += 300

def sugarcoffee() :
    global coffee
    global water
    global frim
    global sugar
    global cup
    global money
    global coin
    coffee = coffee - 10
    frim = frim - 10
    sugar = sugar - 10
    water = water - 100
    cup -= 1
    money -= 300
    coin += 300

def status() :

    print("---------------------------")
    print("재고 현황:")
    print("커피 : {0}g, 프림: {1}g, 설탕: {2}g".format(coffee, frim, sugar))
    print("물 : {0}ml, 종이컵: {1}개".format(water, cup))
    print("자판기 남은 돈:{0}원, 잔돈 현황:{1}원".format(coin, money))
coffee = 500
frim = 500
sugar = 500
water = 1000
cup = 30
coin = 10000



#main
money = int(input("동전을 투입하세요: "))
if(money >= 300) :
    printmenu()
    getmenu = int(input("메뉴를 선택하세요: "))
    while(getmenu != 5) :
        if(getmenu == 1) :
            blackcoffee()
            print("블랙 커피를 선택하셨습니다. 잔돈:", money);
        elif(getmenu == 2) :
            frimcoffee()
            print("프림 커피를 선택하셨습니다. 잔돈:", money);
        elif(getmenu == 3) :
            sugarcoffee()
            print("설탕 프림 커피를 선택하셨습니다. 잔돈:", money);
        elif(getmenu == 4) :
            status();
        elif(getmenu == 5) :
            break;
        else :
            print("다시 입력하세요")
        if(money < 300) :
            print("잔돈이 부족해서 종료합니다.")
            break;
        printmenu();
        getmenu = int(input("메뉴를 선택하세요: "))
        
    


else :
    print("돈이 부족합니다 {0}원:".format(money))


print("---------------------------")
print("커피 자판기 동작을 종료합니다.")
print("---------------------------")
