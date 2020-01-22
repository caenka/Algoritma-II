import csv
import os

while True :
  menu = ['1. Data barang', '2. Pencarian Barang', '3. Penjualan', '4.Stok']
  submenu1 = ['1.list barang', '2.input barang', '3.urut data sesuai harga', '4.kembali ke menu']
  DATABASE_FILE = 'database.csv'
  database = []

  #load data dari csv
  with open (DATABASE_FILE) as db_file:
      csv_reader = csv.reader(db_file, delimiter=",")
      for row in csv_reader : #mengulang csvreader
          database.append(row) #row ditambahkan ke array database
      id_barang=int(database[len(database)-1][0])+1 

  os.system("clear")
  print('\t'.join(menu))
  aksi = int (input ("pilihan: "))

  if aksi == 1:
    while True :
      print('\n'.join(submenu1))  
      aksiMenu1 = int (input ("pilih: "))
      
      if aksiMenu1 == 1:
          #menampilkan data dari array database
              print("%2s \t %10s \t %10s" %("ID","NAMA","HARGA"))
              for row in database :
                  print("%2s \t %10s \t %10s" %(row[0],row[1],row[2]))
                  #ngeprint row per index
              print("")
          
      elif aksiMenu1 == 2 :
          with open (DATABASE_FILE, mode='a') as db_file :
              csv_writer = csv.writer(db_file)
              while True :
                  nama_barang = input ("Masukkan Nama:")
                  if nama_barang =='=':
                      break
                  harga_barang = input ("Masukkan Harga:")
                  csv_writer.writerow([id_barang,nama_barang,harga_barang]) #menulis baris ke file csv
                  database.append([id_barang,nama_barang,harga_barang])#menambahkan file csv baru ke database
                  id_barang+=1 #untuk menambahkan id terakhir agar + 1
                  os.system("clear")
                  print ("Barang telah ditambahkan")

      elif aksiMenu1 == 3:
        print(database)

        for i in range (len(database)):
          database[i][2]=int(database[i][2])
        #data = database.copy()
        
        b=len(database)
        for x in range(b-1,0,-1):
          for y in range(x):
            if database[y][2]>database[y+1][2]:
              temp=database[y+1]
              database[y+1]=database[y]
              database[y]=temp
        print("%2s \t %10s \t %10s" %("ID","NAMA","HARGA"))
        for row in database : 
                print("%2s \t %10s \t %10s" %(row[0],row[1],row[2]))
      elif aksiMenu1 == 4 :
        break
      else :
        print("salah input")