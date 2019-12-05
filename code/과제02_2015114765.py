'''
파이썬 과제02
주사위를 던져서 각 면이 나오는 횟수 및 확률을 구하는 프로그램
'''

import random
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
n = int(input("주사위를 던질 회수를 입력하세요 (100이상): "))
if(n >= 100) :
    for i in range(n) :
        randnum = random.randint(1,6)
        if(randnum == 1) :
            count1 += 1
        elif(randnum == 2) :
            count2 += 1
        elif(randnum == 3) :
            count3 += 1
        elif(randnum == 4) :
            count4 += 1
        elif(randnum == 5) :
            count5 += 1
        elif(randnum == 6) :
            count6 += 1
    print("주사위면 1: {0}회/{1}, 확률: {2}".format(count1, n, round(count1/n,3)))
    print("주사위면 2: {0}회/{1}, 확률: {2}".format(count2, n, round(count2/n,3)))
    print("주사위면 3: {0}회/{1}, 확률: {2}".format(count3, n, round(count3/n,3)))
    print("주사위면 4: {0}회/{1}, 확률: {2}".format(count4, n, round(count4/n,3)))
    print("주사위면 5: {0}회/{1}, 확률: {2}".format(count5, n, round(count5/n,3)))
    print("주사위면 6: {0}회/{1}, 확률: {2}".format(count6, n, round(count6/n,3)))
else :
    print("100 이상의 숫자를 입력하세요. 종료합니다.")
