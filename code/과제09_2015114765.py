'''
파이썬 과제09
대구 평균기온분석
'''


import csv
f = open('daegu.csv', encoding='euc_kr')
data = csv.reader(f)
header = next(data)


temp = [0 for x in range(7)]
count = [0 for x in range(7)]
result = [0 for x in range(7)]

for row in data :
    if (int(row[0][0:4]) >= 1970) and (int(row[0][0:4]) <= 2018) :

        if row[4] != '' :
            if row[0][5:7] == '6.':
                temp[0] += float(row[4])
                count[0] += 1
            elif row[0][5:7] == '7.':
                temp[1] += float(row[4])
                count[1] += 1
            elif row[0][5:7] == '8.':
                temp[2] += float(row[4])
                count[2] += 1
            elif row[0][5:7] == '9.':
                temp[3] += float(row[4])
                count[3] += 1
        if row[3] != '':
            if row[0][5:7] == '12':
                temp[4] += float(row[3])
                count[4] += 1
            elif row[0][5:7] == '1.':
                temp[5] += float(row[3])
                count[5] += 1
            elif row[0][5:7] == '2.':
                temp[6] += float(row[3])
                count[6] += 1
f.close()


for i in range(len(result)):
    result[i]=temp[i]/count[i]     

maxTemp = max(result[0],result[1],result[2],result[3])
maxMonth = result.index(maxTemp) + 6
minTemp = min(result[4],result[5],result[6])
if result.index(minTemp) == 4:
    minMonth = 12
elif result.index(minTemp) == 5:
    minMonth = 1
elif result.index(minTemp) == 6:
    minMonth = 2



print("여름철 평균기온:")         
print("6 월 평균 기온: %.2f 도" %(result[0]))
print("7 월 평균 기온: %.2f 도" %(result[1]))
print("8 월 평균 기온: %.2f 도" %(result[2]))
print("9 월 평균 기온: %.2f 도" %(result[3]))
print("대구에서 가장 더운 달은 %d 월이고, 평균기온은 %.2f 도 였습니다."%(maxMonth,maxTemp))
print("\n겨울철 평균 기온:")
print("12 월 평균 기온: %.2f 도"%(result[4]))
print("1 월 평균 기온: %.2f 도" %(result[5]))
print("2 월 평균 기온: %.2f 도" %(result[6]))
print("대구에서 가장 추운 달은 %d 월이고, 평균기온은 %.2f 도 였습니다."%(minMonth,minTemp))
