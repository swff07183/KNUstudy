'''
파이썬 과제11
대구 인구 비율분석
'''



import csv
import matplotlib.pyplot as plt
import platform

male = [0 for x in range (8)]
female = [0 for y in range (8)]
region = ['중구', '동구', '서구', '남구', '북구', '수성구', '달서구', '전체']

f = open('gender.csv', encoding='euc_kr')
data = csv.reader(f)
header = next(data)

for row in data:
    if '대구광역시' in row[0]:
        if region[0] in row[0] :
            male[0] += int(row[1].replace(",",""))
            female[0] += int(row[105].replace(",",""))
        elif region[1] in row[0] :
            male[1] += int(row[1].replace(",",""))
            female[1] += int(row[105].replace(",",""))
        elif region[6] in row[0] :
            male[6] += int(row[1].replace(",",""))
            female[6] += int(row[105].replace(",",""))
        elif region[2] in row[0] :
            male[2] += int(row[1].replace(",",""))
            female[2] += int(row[105].replace(",",""))
        elif region[3] in row[0] :
            male[3] += int(row[1].replace(",",""))
            female[3] += int(row[105].replace(",",""))
        elif region[4] in row[0] :
            male[4] += int(row[1].replace(",",""))
            female[4] += int(row[105].replace(",",""))
        elif region[5] in row[0] :
            male[5] += int(row[1].replace(",",""))
            female[5] += int(row[105].replace(",",""))
            
        #남_총인구수 : row[1], 여_총인구수 : row[105]
f.close()

for i in range(7) :
    male[i], female[i] = male[i]/2, female[i]/2
    male[7] += male[i]
    female[7] += female[i]
gender = ['남성', '여성']
color = ['steelblue', 'darkorange']



if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
else:
    plt.rc('font', family='AppleGothic')

fig, axes = plt.subplots(2, 4, figsize=(10, 5), sharex = True, sharey = True)

for i in range(8) :
    plt.subplot(2, 4, i+1)
    plt.pie([male[i], female[i]], labels = gender, autopct='%.1f%%', colors=color, startangle=90)
    plt.title('대구광역시 '+ region[i], fontsize = 10)
    

plt.show()
