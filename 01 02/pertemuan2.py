#datatunggal
#String
a = ('python pemula')
print(type(a))

#integer
b = 12
print(type(b))

#boolean
c = True
print(type(c))

#float
d = 9.5
print(type(d))

#data berkelompok
#list
angka = [1,2,3,4,5]
print(type(angka))
print(angka[0])
pakaian = ["baju", "celana", "kaos", "topi"]
print(pakaian[2])
print(pakaian[0:2])
print(pakaian[:3])
print(pakaian[2:])

hewan = ["Burung", "Kecoa", "Tikus"]
print(hewan)
hewan.append("Singa") #fungsi append untuk menambahkkan item ke list
print(hewan)

jurusan = ["Informatika", "Komputer", "Elektro"]
print(jurusan)
jurusan.insert(1, "Akuntansi") #insert untuk menambahkan item pada indeks tertentu
print(jurusan)

buah = ["jeruk", "semangka"]
nomor = [1,2]
buah.extend(nomor)
print(buah)

rokok = ["sampurna mild", "sampurna kretek", "surya12", "surya16"]
rokok.remove("surya12") #untuk menghapus item
print(rokok)

rokok = ["sampurna mild", "sampurna kretek", "surya12", "surya16"]
rokok.pop(1)
print(rokok)

rokok = ["sampurna mild", "sampurna kretek", "surya12", "surya16"]
rokok.clear() #untuk menghapus semua item pada list
print(rokok)
#list sebagai itterable
gorengan = ["tempe goreng", "bakwan", "cireng", "ubi goreng"]
for g in gorengan:
  print(g)

#string sebagai itterable
nama = 'muhammad nur sodiq'
for n in nama:
  print(n)

#for didalam for
buah1 = ['semangka', 'jeruk', 'apel', 'anggur']
sayur = ['kangkung', 'bayam', 'wortel']

DaftarBelanja =[gorengan,buah1,sayur]

for subDaftarBelanja in DaftarBelanja:
  print(subDaftarBelanja)
  for komponen in subDaftarBelanja:
    print(komponen)







print("===================================================")
#tuple
nilai = (1,2,3,4,5)
print(nilai)
print(type(nilai))

#dictionary
biodata =	{
  "Nama": "Muhammad Nur Sodiq",
  "Nim": "181111114",
  "Prodi": "Informatika",
  "Angkatan" : 2018
}
print(biodata)
print(type(biodata))
print(biodata["Prodi"])
print(len(biodata)) #untuk menghitung jumlah data
