'''
파이썬 과제07
주민등록번호 정상 판별 프로그램
'''

class idnumber :
    
    def __init__(self) :
        while(True) :
            inputnum = input("주민등록번호를 숫자만 입력하세요: ")
            if(inputnum.isdigit() and len(inputnum) == 13) :
                self.id = inputnum
                break
            
            elif (len(inputnum) < 13) :
                print("입력된 숫자의 자리수가 13자리 이하입니다. 다시 입력하세요")
            elif (len(inputnum) > 13) :
                print("주민등록번호가 13자리 보다 큽니다. 다시 입력하세요.")
            elif ('-' in inputnum) :
                print("-를 빼고 다시 입력하세요.")
            elif (' ' in inputnum) :
                print("공백 문자가 포함되었습니다. 다시 입력하세요.")
            elif (x.isalpha() for x in inputnum) :
                print("알파벳 문자가 포함되었습니다. 다시 입력하세요.")
            
        
    def check(self) :
        # 정상 또는 비정상 출력
        self.check_error_num()
        self.check_city()
        if(self.checknum == int(self.id[-1])) :
            print("정상적인 주민등록번호입니다.")
            if (int(self.id[0:2]) > 19) :
                print("성인 인증이 되었습니다. 나이 %d세" %(119 - int(self.id[0:2])))
            else :
                if(int(self.id[0:2]) == 0) :
                    print("성인 인증이 되었습니다. 나이 %d세" %(19 - int(self.id[0:2])))
                else :
                    print("미성년자입니다. 나이 %d세" %(19 - int(self.id[0:2])))
            print("주민등록번호: %s" %(self.id))
            print("생년월일: %s" %(self.id[0:6]))
            print("출생지: %s" %(self.city))
        else :
            print("불법 생성된 주민등록번호입니다.")
        
    def check_error_num(self) :
        # 오류 검증 번호
        sum = 0
        for i in range(12) :
            if(i < 8) :
                sum += (i + 2) * int(self.id[i])
            else :
                sum += (i - 6) * int(self.id[i])
                
        self.checknum = (11 - (sum % 11)) % 10


    def check_city(self) :    
        # 과제1
        a = (int(self.id) // 10000) % 100
        if((a >= 0) and (a <= 8)) :
            self.city = "서울"
        elif((a >= 9) and (a <= 12)) :
            self.city = "부산"
        elif((a >= 13) and (a <= 15)) :
            self.city = "인천"
        elif((a >= 16) and (a <= 25)) :
            self.city = "경기"
        elif((a >= 26) and (a <= 34)) :
            self.city = "강원"
        elif((a >= 35) and (a <= 47)) :
            self.city = "충청"
        elif((a >= 48) and (a <= 66)) :
            self.city = "전라"
        elif((a >= 67) and (a <= 91)) :
            self.city = "경상"
        elif((a >= 92) and (a <= 95)) :
            self.city = "제주"
        else :
            self.city = "?"

Hong = idnumber()
Hong.check()
