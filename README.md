# lab-5
## Tugas Praktikum 5

![soal-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/1.png)

**Code**

![sc-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/2.png)
![sc-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/3.png)
![sc-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/4.png)
![sc-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/5.png)

**Penjelasan:**
* ``data={}`` list dengan format dictionary
* Gunakanlah perulangan ``While`` untuk menampilkan data sebanyak banyaknya
* ``menu = input("(T)ambah, (U)bah, (H)apus, (L)ihat, (C)ari, (K)eluar: ")`` kita tambahkan input Tambah, Ubah, Hapus, Lihat, Cari, Keluar dalam variabel menu
* masukan nama, nim, nilai_tugas, nilai_uts, nilai_uas, dan nilai_akhir. nilai akhir didapat dari = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100 
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
* ``sub_data = input("(Semua), (Nama), (NIM), (Tugas), (UTS), (UAS) : ")`` memmbuat menu ubah di dalam ``sub_data``
* ``if sub_data.lower() == "semua":`` ambil kata kunci 'semua' di dalam ``sub_data`` jika 'semua' maka input ``data[nama][1] = input("Ubah NIM:") data[nama][2] = int(input("Ubah Nilai Tugas: ")) data[nama][3] = int(input("Ubah Nilai UTS: ")) data[nama][4] = int(input("Ubah Nilai UAS: "))``
* ``data[nama][5] = data[nama][2] *30/100 + data[nama][3]*35/100 + data[nama][4] *35/100 `` kita dapatkan nilai akhir dengan diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%), *ket: [5] = nilai_akhir, dimana [0] = nama*
* 
**Output:**

Tambah data

![output-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/t.png)


Ubah data

![output-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/u.png)


Hapus data

![output-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/h.png)


Lihat data

![output-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/l.png)


Cari data

![output-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/c.png)


**Flowchart:**

![output-praktikum-5](assets/img/tugas-praktikum-5/tugas-praktikum/flowchart.png)