'''
파이썬 과제05
소수 구하기 : 에라토스테네스의 체
'''

def primenum(array, mulnum) :
    print("Remove {0}'s multiple numbers".format(mulnum))
    for x in range (len(array)) :
        if(array[x] != 'X') :
            if(array[x] != mulnum and array[x] % mulnum == 0) :
                array[x] = 'X'
    printarr(array)

def printarr(arr) :
    for i in range(len(arr)) :
        print("%4s" %str(arr[i]),end = " ")
        if( (i+1) % 10 == 0) :
            print("")
    print("")



num2to100 = list(range(2,101))

print("Original number =>")
printarr(num2to100)
primenum(num2to100, 2)
primenum(num2to100, 3)
primenum(num2to100, 5)
primenum(num2to100, 7)
print("Prime numbers: ")
printarr(num2to100)

