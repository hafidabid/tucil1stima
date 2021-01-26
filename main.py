import datetime as dt

def permutationEngine(arr,arrSize,tabungan=9):
    if(arrSize==1):
        if str(arr[0])!='0' and str(arr[1])!='0':
            if int(arr[1])>tabungan:
                return []
            else:
                return arr
        else:
            return []
    else:
        res = []
        for y in range(arrSize):
            res = res+permutationEngine(arr,arrSize-1,tabungan)
            if(arrSize%2==1):
                arr[0],arr[arrSize-1] = arr[arrSize-1],arr[0]
            else:
                arr[y],arr[arrSize-1] = arr[arrSize-1],arr[y]

        return res

def pisahkan(arr,n):
    res = []
    temp = []
    count = 0
    for x in arr:
        if count<n:
            temp.append(x)
            count=count+1
        else:
            res.append(temp)
            temp=[]
            temp.append(x)
            count = 1

    res.append(temp)
    return res

def getHuruf(arrofinput):
    r = list()
    r.append(arrofinput[0][0])
    temp = arrofinput[len(arrofinput)-1][0]
    if (not(temp in r)):
        r.append(temp)
    else:
        t=1
        while arrofinput[t][0] in r and arrofinput[t]!="------":
            t =t +1
        r.append(arrofinput[t][0])
        r[0],r[1] = r[1],r[0]

    for x in arrofinput:
        if (x!="------"):
            for y in x:
                if (not(y in r)):
                    r.append(y)

    return r

def kombinatorial(arr,n,pos0,res):
    if(n==0):
        return res
    else:
        reslt = []
        for x in range(pos0,len(arr)-n+1):
            res[len(res)-n] = arr[x]
            reslt = reslt + kombinatorial(arr,n-1,x+1,res)

        return reslt

def getPermutasiAnkga(n,tabungan = 9):
    arr = [x for x in range(10)]
    if n<10:
        a1 = pisahkan(kombinatorial(arr,n,0,[0 for x in range(n)]),n)
        a2 = []
        for z in a1:
            a2 = a2 + permutationEngine(z,len(z),tabungan)

        return pisahkan(a2,n)
    elif n==10:
        return pisahkan(permutationEngine(arr,10,tabungan),10)
    else:
        return []

def pencocokan(arrHuruf,arrAngka,huruf):
    if len(arrAngka)==len(arrHuruf):
        flag = False
        c = 0
        while c<len(arrHuruf) and flag==False:
            if arrHuruf[c] == huruf:
                flag=True
            else:
                c=c+1

        if flag:
            return arrAngka[c]
        else:
            return -1
    else:
        return -1

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

def criptaarimatic(arr,listhuruf,listangka):
    angka = []
    flag = True
    count = 0

    if len(listhuruf)>0:
        while (count < len(arr) and flag):
            if arr[count] != "------":
                temp = ""
                for y in arr[count]:
                    temp = temp + str(pencocokan(listhuruf, listangka, y))

                if temp[0] == "0": flag = False
                angka.append(int(temp))

            count = count + 1
    else:
        while (count < len(arr) and flag):
            if arr[count] != "------":
                temp = ""
                for y in arr[count]:
                    temp = temp + str(cariangka(listangka, y))

                if temp[0] == "0": flag = False
                angka.append(int(temp))

            count = count + 1

    count = 0
    if flag:
        for x in range(len(angka) - 1):
            count = count + angka[x]

        if count == angka[len(angka) - 1]:
            return {
                'status': True,
                'data': angka
            }
        else:
            return {
                'status': False,
                'data': angka
            }
    else:
        return {
            'status':False,
            'data' : []
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
    menabung = cekTabunganAngka(data)
    #print(menabung)
    listhuruf = getHuruf(data)
    pasangan_angka = getPermutasiAnkga(len(listhuruf),menabung)
    #print("finish permutasi = "+str((dt.datetime.today()-starttime).total_seconds())+" detik")
    #print(len(pasangan_angka))
    test = 0
    reslt = 0

    if len(listhuruf)<9:
        for variasi in pasangan_angka:
            test = test + 1
            hasil_cripta = criptaarimatic(data, listhuruf, variasi)
            # print(hasil_cripta)
            if hasil_cripta['status']:
                reslt = reslt + 1
                printSolution(data, hasil_cripta['data'], reslt)
                print("percobaan ke = " + str(test)+"/"+str(len(pasangan_angka)))
                waktu = (dt.datetime.today() - starttime).total_seconds()
                print("waktu dibutuhkan = " + str(waktu) + " detik")
                print()
    else:
        for v in range(len(pasangan_angka)-1,-1,-1):
            test = test+1
            hasil_cripta = criptaarimatic(data, listhuruf, pasangan_angka[v])
            if hasil_cripta['status']:
                reslt = reslt + 1
                printSolution(data, hasil_cripta['data'], reslt)
                print("percobaan ke = " + str(test)+"/"+str(len(pasangan_angka)))
                waktu = (dt.datetime.today() - starttime).total_seconds()
                print("waktu dibutuhkan = " + str(waktu) + " detik")
                print()

def cekTabunganAngka(data):
    n = len(data[len(data)-1])
    la = len(data)
    c = 0
    for x in data:
        if x!="------" and x!=data[len(data)-1] and len(x)+1==n:
            c=c+1
        elif(x!="------" and x!=data[len(data)-1] and len(x)>=n):
            #print(x)
            return 9

    if c>1:
        return c-1
    else:
        return 2

inputan = str((open('input.txt','r')).read()).split()
h = getHuruf(inputan)
print("banyak komponen huruf = "+str(len(h))+" \n")
starttime= dt.datetime.today()
bruteforce(inputan,starttime)
endtime = dt.datetime.today()
print("\nFINISH ALL IN = "+str((endtime-starttime).total_seconds())+" SECOND")