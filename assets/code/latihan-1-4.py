# list-bebas
a = [1, 3, 5, 7, 9] 

# akses list
print(a[2]) #tampilkan elemen ke - 3

print(a[1:3]) #ambil nilai elemen ke 2 sampai elemen ke 4

print(a[4]) #ambil elemen terakhir

print('----------------------------------------------')

# ubah elemen list
a[3] = 4 #ubah elemen ke 4 dengan nilai lainnya
print(a)

a[3:5] = [8, 10] #ubah elemen ke 4 sampai dengan elemen terakhir
print(a)

print('----------------------------------------------')

# tambah elemen list
b = a [0:2] #ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
print(b)

b.append('halo') #tambah list B dengan nilai string
print(b)

b.extend([10, 20, 30]) #tambah list B dengan 3 nilai
print(b)

x = a + b #gabungkan list B dengan list A
print(x)
