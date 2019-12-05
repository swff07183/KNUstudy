'''
파이썬 과제10
대규 일교차 분석
'''

import csv
import matplotlib.pyplot as plt

temp = [[0 for y in range(12)] for x in range(10)]
count = [[0 for y in range(12)] for x in range(10)]
f = open('daegu.csv', encoding='euc_kr')
data = csv.reader(f)
header = next(data)

for row in data :
    if (int(row[0][0:4]) >= 2009) and (int(row[0][0:4]) <= 2018) :
        if(row[3] != '' and row[4] != '') :
            #print(row[0], float(row[4]) - float(row[3]))
            date = row[0].split('.')
            date[0], date[1], date[2] = int(date[0]), int(date[1]), int(date[2])
            #print(date)
            temp[date[0]-2009][date[1]-1] += float(row[4])-float(row[3])
            count[date[0]-2009][date[1]-1] += 1
            
maxtemp = [0 for x in range(10)]
maxmonth = [0 for y in range(10)]
for i in range(10) :
    for j in range(12) :
        temp[i][j] /= count[i][j]
        temp[i][j] = round(temp[i][j],1)
    maxtemp[i] = max(temp[i])
    maxmonth[i] = str(i + 2009) +'.'+ str(temp[i].index(max(temp[i]))+1)


print()
print("대구 월별 평균 일교차")
for i in range(10) :
    print("{0} : {1}".format(maxmonth[i] ,maxtemp[i]))
plt.figure(figsize=(10, 5)) 
plt.rc('font', family='Malgun Gothic') 
plt.title("2019년부터 2018년까지 대구의 평균 일교차가 가장 큰 달")
plt.bar(maxmonth, maxtemp)
plt.show()
