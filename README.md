# lab-4
## Latihan 1
![soal-latihan-1](assets/img/tugas-praktikum-4/latihan1/1.png)

**Code:**

![sc-latihan-1](assets/img/tugas-praktikum-4/latihan1/2.png)

**Penjelasan:**
* ``a = [1, 3, 5, 7, 9] `` list a dengan 5 elemen

Akses list
* ``print(a[2])`` menampilkan elemen ke - 3
* ``print(a[1:3])`` mengambil nilai elemen ke 2 sampai elemen ke 4
* ``print(a[4])`` mengambil elemen terakhir

ubah elemen list
* ``a[3] = 4`` mengubah elemen ke 4 dengan nilai lainnya
* ``a[3:5] = [8, 10]`` mengubah elemen ke 4 sampai dengan elemen terakhir

tambah elemen list
* ``b = a [0:2]`` mengambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
* ``b.append('halo')`` menambah list B dengan nilai string
* ``b.extend([10, 20, 30])`` menambah list B dengan 3 nilai
* ``x = a + b`` menggabungkan list B dengan list A

**Output:**

![output-latihan-1](assets/img/tugas-praktikum-4/latihan1/3.png)

## Tugas Praktikum 4
![soal-praktikum-1](assets/img/tugas-praktikum-4/tugas-praktikum/1.png)

**Code:**

![sc-praktikum-1](assets/img/tugas-praktikum-4/tugas-praktikum/2.png)

**Penjelasan:**
* ``data = []`` Membuat list kosong yang nanti akan di isi
* ``while ulangi =='y':`` Membuat perulangan dengan variabel ``ulangi``, dimana ketika memilih 'y' maka akan otomatis mengulang pengisian data
* ``nilai_akhir = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100`` Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%)
* ``data.append([nama, nim, nilai_tugas, nilai_uts, nilai_uas, int(nilai_akhir)])`` Memasukkan variabel input ke dalam list data
* ``ulangi = (input('tambah data?(y/t)'))`` Ketika memilih 't' ``if ulangi == 't':`` maka cetaklah hasil 

**Output:**

![output-praktikum-1](assets/img/tugas-praktikum-4/tugas-praktikum/3.png)

**Flowchart:**


<div align="center">
  <img alt="flowchart-praktikum-1" src="assets/img/tugas-praktikum-4/tugas-praktikum/4.png" />
</p>


# lab-5
## Latihan 1

* Belom

## Tugas Praktikum 5

![soal-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/1.png)

**Code:**

![sc-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/2.png)
![sc-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/3.png)
![sc-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/4.png)
![sc-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/5.png)

**Penjelasan:**

**Header**
* ``data={}`` untuk menampung list dengan format dictionary
* Gunakanlah perulangan ``While`` untuk menampilkan data sebanyak banyaknya
* ``menu = input("(T)ambah, (U)bah, (H)apus, (L)ihat, (C)ari, (K)eluar: ")`` kita tambahkan input Tambah, Ubah, Hapus, Lihat, Cari, Keluar dalam variabel menu
* ``else: print("Upss ada yang salah, silahkan cek kembali.")`` jika kita salah dalam input maka akan tercetak 'Upss ada yang salah, silahkan cek kembali.'
* masukan nama, nim, nilai_tugas, nilai_uts, nilai_uas, dan nilai_akhir yang nanti akan di masukkan kedalam ``data={}``
* Nilai akhir didapat dari = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100 

**Keluar**
* ``if menu.lower() == 'k':`` Ambil data 'k' dari ``menu`` 
* lalu ``break`` untuk menghentikan seluruh proses

**Lihat data**
* ``elif menu.lower() == 'l':`` Kita menggunakan kondisi percabangan if, ambil data dari ``menu`` lalu kita akan mengubah perintah 'l' yang kita input menjadi huruf kecil dengan fungsi ``lower()``
* lalu cetak ``print()``

**Tambah data**
* ``elif menu.lower() == 't':`` Ambil data 't' dari ``menu`` 
* ``nama = input("Masukan nama: ")`` lalu tambahkan input nama, nim, nilai tugas, uts, uas
* ``nilai_akhir = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100 `` untuk nilai akhir diambil dari perhitungan 3 komponen nilai (nilai_tugas: 30%, nilai_uts: 35%, nilai_uas: 35%)
* ``data[nama] = [nama, nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir]`` kita akan masukkan data yang tadi kita input ke dalam `data[nama]'
* lalu cetak ``print()``

**Ubah data**
* ``elif menu.lower() == 'u':`` Ambil data 'u' dari ``menu`` 
* ``nama = input("Masukan nama untuk mengubah data: ")`` kita akan menginput data yang nanti akan di ubah
* ``if nama in data.keys(): print("Mau mengubah apa?")`` jika 'nama' dari di dalam 'data' maka akan mengembalikan daftar menggunakan fungsi 'keys()' lalu di cetak lah 'print()'
* ``sub_data = input("(Semua), (Nama), (NIM), (Tugas), (UTS), (UAS) : ")`` membuat menu ubah di dalam ``sub_data``
* ``if sub_data.lower() == "semua":`` ambil kata kunci 'semua' di dalam ``sub_data`` jika 'semua' maka input ``data[nama][1] = input("Ubah NIM:") data[nama][2] = int(input("Ubah Nilai Tugas: ")) data[nama][3] = int(input("Ubah Nilai UTS: ")) data[nama][4] = int(input("Ubah Nilai UAS: "))``
* ``data[nama][5] = data[nama][2] *30/100 + data[nama][3]*35/100 + data[nama][4] *35/100 `` kita dapatkan nilai akhir dengan diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%), 

*ket: [5] = nilai_akhir, dimana [0] = nama*

* lalu cetak ``print("\nBerhasil ubah data!")``
* Jika kita ingin mengubah data tertentu maka ``elif sub_data.lower() == "nim": data[nama][1] = input("NIM:")`` dan berlaku juga untuk nilai tugas, UTS dan UAS
* lalu cetak ``print("\nBerhasil ubah data!")``
* ``else: print("'{}' tidak ditemukan.".format(nama))`` jika kita salah dalam memasukkan nama untuk mengubah data maka akan muncul 'nama tidak di temukan'

**Cari data**
* ``elif menu.lower() == 'c':`` Ambil data 'c' dari ``menu`` 
* ``nama = input("Masukan nama untuk mencari data: ")`` kita akan menginput data yang nanti akan di cari
* ``if nama in data.keys():`` kita mengambil list 'nama' di dalam 'data' menggunakan pengkondisian
* maka cetak ``print("Nama: {0}\nNIM : {1}\nNilai Tugas: {2}\nUTS: {3}\nUAS: {4}\nNilai akhir: {5}"`` untuk menampilkan data yang tersedia
* ``else: print("'{}' tidak ditemukan.".format(nama))`` jika data yang kita input salah/tidak ditemukan maka akan tercetak 'nama tidak di temukan'

**Hapudata**
* ``elif menu.lower() == 'h':`` Ambil data 'h' dari ``menu`` 
* ``nama = input("Masukan nama untuk menghapus data : ")`` kita akan menginput data yang nanti akan di hapus
* ``if nama in data.keys():`` kita mengambil list 'nama' di dalam 'data' menggunakan pengkondisian
* ``del data[nama]`` hapus semua 'nama'  yang ada di dalam 'data'
* jika sudah maka cetak ``print("sub_data '{}' berhasil dihapus.".format(nama))``
* ``else: print("'{}' tidak ditemukan.".format(nama))`` jika data yang kita input salah/tidak ditemukan maka akan tercetak 'nama tidak di temukan'



**Output:**

Tambah data

![output-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/t.png)


Ubah data

![output-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/u.png)


Lihat data

![output-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/l.png)


Cari data

![output-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/c.png)


Hapus data

![output-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/h.png)


**Flowchart:**


![output-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/flowchart.png)