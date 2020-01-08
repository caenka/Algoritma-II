print ("Selamat Datang di Biro Jodoh")
print ("\n")

import random

print ("1 = laki_laki")
print ("2 = perempuan")
dftrcewek = []
dftrcowok = []
nilai = []
hasil =0
z = []
while True :
    pilihan = input("Apa Jenis kelamin anda :")
    if pilihan == "1":
        jumlahcewek = int(input("Berapa jumlah pasangan anda?"))
        for i in range(jumlahcewek):
            cewekInput = input ("Masukan nama cewek :")
            dftrcewek.append(cewekInput)
        cowok = input ("Masukan nama cowok : ")
        print ("\n===================")
        print ("Nama cowok :" ,cowok.split(" ")[0])
        for j in dftrcewek:
            print ("Nama cewek:", j.split(" ")[0])
                       
        for j in range(len(dftrcewek)):
            match = random.randrange(1,100)
            hasil = hasil + match
            nilai.append(hasil)
            hasil=0
            print("Akurasi cewek "+str(j+1)+":"+str(match)+"%")

            if match > 80 :
                print ("ndang rabi")
            elif match >60 :
                print ("pikir-pikir")
            elif match >40 :
                print ("yakin ?")
            elif match >20:
                print ("cari lagi")
            else :
                print ("putus aja")
        result=zip()
        result=list(zip(dftrcewek,nilai))
        for k in range(len(result)):
            u=result[k][1],result[k][0]
            z.append(u)
            q=max(z)
        print (cowok, "Cocok dengan",q[1])

        break

    elif pilihan=="2":
        jumlahcowok = int(input("Berapa jumlah pasangan anda?"))
        for i in range(jumlahcowok):
            cowokInput = input ("Masukan nama cowok :")
            dftrcowok.append(cowokInput)
        cewek = input ("Masukan nama cewek : ")
        print ("\n===================")
        print ("Nama cewek :" ,cewek.split(" ")[0])
        for j in dftrcowok:
            print ("Nama cowok:", j.split(" ")[0])
                       
        for j in range(len(dftrcowok)):
            match = random.randrange(1,100)
            hasil = hasil + match
            nilai.append(hasil)
            hasil=0
            print("Akurasi cowok "+str(j+1)+":"+str(match)+"%")

            if match > 80 :
                print ("ndang rabi")
            elif match >60 :
                print ("pikir-pikir")
            elif match >40 :
                print ("yakin ?")
            elif match >20:
                print ("cari lagi")
            else :
                print ("putus aja")

        result=zip()
        result=list(zip(dftrcowok,nilai))
        for k in range(len(result)):
            u=result[k][1],result[k][0]
            z.append(u)
            q=max(z)
        print (cewek, "Cocok dengan",q[1])

        break
    
    else :
        break

        
