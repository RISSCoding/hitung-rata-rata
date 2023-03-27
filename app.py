#Meminta pengguna untuk memasukkan nilai numerik, pisahkan dengan koma
input_str = input("Masukkan nilai-nilai numerik, pisahkan dengan koma: ")

#Menisahkan nilai-nilai numerik menjadi List
nilai_list = input_str.split(",")

#Mengubah nilai dalam list dari string menjadi float
nilai_list = [float(nilai) for nilai in nilai_list]

#Menghitung rata-rata dari nilai dalam List
rata_rata = sum(nilai_list) / len(nilai_list)

#Mencetak hasil rata-rata
print("Nilai rata-ratanya adalah:", rata_rata)