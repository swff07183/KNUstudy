'''
파이썬 과제08
RandomIntList클래스
'''


import random

    
class RandomIntList(list) :
    def __init__(self, start, end) :
        self.lists = []
        for i in range(start, end + 1) :
            self.lists.append(random.randint(start, end))

    def __repr__(self):
        printlist = ""
        for i in range(len(self.lists)) :
            printlist += "[%2s]"%str(i)
        printlist += "\n["
        for i in range(len(self.lists)-1) :
            printlist += "%3s,"%str(self.lists[i])
        printlist += "%3s ]"%str(self.lists[len(self.lists)-1])
        return printlist

    def replace(self, old, new):
        count = 0
        while old in self.lists :
            self.lists[self.lists.index(old)] = new
            count += 1

        if(count == 0) :
            print("{0}가 리스트에 없습니다.".format(old))
        else :
            print("{0}개의 {1}가 {2}로 교체되었습니다.".format(count, old, new))
            
    def dremove(self):
        a = []
        for i in range(len(self.lists)) :
            if self.lists[i] not in a :
                a.append(self.lists[i])
        self.lists = a

    def removeall(self, x) :
        count = 0
        while x in self.lists :
            self.lists.remove(x)
            count += 1

        print("{0} 를 {1}개 삭제하였습니다.".format(x, count))
        return self.lists



def main() :
    startnum = input("시작과 끝을 입력하세요.")
    start, end = startnum.split()
    start, end = int(start), int(end)

    a = RandomIntList(start, end)
    print(a)
    
    while(True) :
        print("RandomIntList 테스트")
        print("1. 리스트 출력")
        print("2. replace(old, new)")
        print("3. dremove(): 중복 item 제거")
        print("4. removeall(x): 모든 x 삭제")
        print("5. 종료")
        selectmenu = int(input("메뉴를 선택하세요: "))
        if(selectmenu == 5) :
            break;
        elif(selectmenu == 1) :
            print(a)
        elif (selectmenu == 2):
            inputnum = input("교체할 숫자 (old, new) 입력(공백 구분): ")
            old , new = inputnum.split()
            old , new = int(old), int(new)
            a.replace(old, new)
            print(a)
        elif (selectmenu == 3):
            a.dremove()
            print(a)
        elif (selectmenu == 4):
            removenum = int(input("삭제할 숫자를 입력하세요: "))
            a.removeall(removenum)
            print(a)

main()
