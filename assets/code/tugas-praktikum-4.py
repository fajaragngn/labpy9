# Buat program sederhana untuk menambahkan data ke dalam sebuah list
data = []
ulangi = 'y'

while ulangi =='y':
    nama = input("NAMA :")
    nim = input("NIM :")
    nilai_tugas = int(input("Nilai Tugas :"))
    nilai_uts = int(input("Nilai UTS :"))
    nilai_uas = int(input("Nilai UAS :"))
    nilai_akhir = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100 

    data.append([nama, nim, nilai_tugas, nilai_uts, nilai_uas, int(nilai_akhir)])

    ulangi = (input('tambah data?(y/t)'))
    if ulangi == 't':
        print("\n                            Daftar Nilai")
        print("==================================================================")
        print("|No. |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
        print("==================================================================")
        i = 0
        for item in data:
            i += 1
            print("| {no:2d} | {nama:12s} | {nim:9s} | {nilai_tugas:5d} | {nilai_uts:5d} | {nilai_uas:5d} | {nilai_akhir:6.2f} |"
                .format(no=i, nama=item[0], nim=item[1], nilai_tugas=item[2], nilai_uts=item[3], nilai_uas=item[4], nilai_akhir=item[5]))
        print("==================================================================")

