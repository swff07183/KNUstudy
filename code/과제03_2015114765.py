'''
파이썬 과제03
로또 번호 생성 프로그램
'''
import random

def lotto(howmany) :
    print("로또 번호")
    for i in range(howmany):
        lotto = ""
        for j in range (6) :
            random_num = random.randint(1, 45)
            lotto = lotto + "%2s " %str(random_num)
        print("[ %d ]: " %(i+1), lotto)

while (True) :
    print("")
    howmany = int(input("로또를 몇장 구매하시겟습니까? "))
    print("")
    if(howmany == 0) :
        break;
    
    lotto(howmany)

print("종료합니다.")
