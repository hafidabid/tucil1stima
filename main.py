#tucil 1 strategi algoritma
'''
Hafid Abi Daniswara
13519028
tucil 1: brute force
'''

import datetime
import permutasiii as pt

def getHuruf(arrofinput):
    r = list()
    for x in arrofinput:
        if (x!="------"):
            for y in x:
                if (not(y in r)):
                    r.append(y)

    return r

def permutasi(params):
    z = 0
    for x in params:
        z=z+1

    if(z<10):
        return permutasi(params+list("*"))
    elif(z>10):
        print("maksimal 10 huruf!!!")
        return []
    else:
        return pt.pisahkan(pt.heapPermutation(params,len(params)),10)

def cariangka(arr,huruf):
    count = 0
    flag = False
    while(flag==False):
        if(arr[count]==huruf):
            flag = True
        else:
            count=count+1

    if flag:
        return count
    else:
        return 0-1

def criptaarimatic(arr,listangka):
    angka = []
    flag = True
    for x in arr:
        if x!="------":
            temp = ""
            for y in x:
                temp = temp + str(cariangka(listangka, y))

            angka.append(int(temp))

    count = 0
    for x in range(len(angka)-1):
        count = count+angka[x]

    if count==angka[len(angka)-1]:
        return {
            'status' : True,
            'data'  : angka
        }
    else:
        return {
            'status' : False,
            'data'  : angka
        }

def printSolution(arr0,arr1,index):
    print("Solusi ke-"+str(index))
    count =0
    longest_length = len(arr0[len(arr0)-1])+1
    while(arr0[count]!="------"):
        spacing = longest_length-len(arr0[count])
        for x in range(spacing): print(' ',end='')
        print(arr0[count],end='')
        print('   ',end='')
        spacing = spacing+(len(arr0[count])-len(str(arr1[count])))
        for x in range(spacing): print(' ', end='')
        print(arr1[count])
        count=count+1

    print("+",end='')
    for x in range(longest_length-1):print("-",end='')
    print('   +',end='')
    for x in range(longest_length - 1): print("-", end='')
    print()
    print(" "+arr0[len(arr0)-1]+"    "+str(arr1[len(arr1)-1]))

def bruteforce(data,starttime):
    listhuruf = getHuruf(data)
    permutasi_huruf = permutasi(listhuruf)
    test = 0
    reslt = 0
    for variasi in permutasi_huruf:
        test = test + 1
        hasil_cripta = criptaarimatic(data,variasi)
        #print(hasil_cripta)
        if hasil_cripta['status']:
            reslt = reslt+1
            printSolution(data,hasil_cripta['data'],reslt)
            print("percobaan ke = "+str(test))
            waktu = (datetime.datetime.today() - starttime).total_seconds()
            print("waktu dibutuhkan = "+ str(waktu) +" detik")
            print()


inputan = str((open('input.txt','r')).read()).split()
starttime= datetime.datetime.today()
bruteforce(inputan,starttime)

'''
arrhuruf = ['*', 'E', 'N', 'D', 'M', 'O', 'R', 'Y','S','*']
inputan = str((open('input.txt','r')).read()).split()
print(inputan)
criptaarimatic(inputan,arrhuruf)
'''

'''
inputan = str((open('input.txt','r')).read()).split()
asd = getHuruf(inputan)
starttime= datetime.datetime.today()
hasl = permutasi(asd)
print(hasl)
print(len(hasl))
finishtime= datetime.datetime.today()
print(starttime)
print(finishtime)
'''

