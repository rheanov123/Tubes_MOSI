import random

#inisialisasi variabel scalar
jumlah_individu = 200
terinfeksi = jumlah_individu * 0.05
probabilitas_bergerak = 0.8
waktu_pemulihan = 10


#ukuran ruang simulasi
x_min = 0
y_min = 0
x_max = 20
y_max = 20

x_range = x_max-x_min
y_range = y_max-y_min
x_position = []
y_position = []

terinfeksi=[]
waktu_infeksi=[]


for individu in range(jumlah_individu):
    x_position.append(random.randint(x_min,x_max))
    y_position.append(random.randint(y_min,x_max))

    #status terinfeksi
    if (individu < terinfeksi):
        terinfeksi.append(True)
    else:
        terinfeksi.append(False)

    # initial status imune
    imunitas.append(False)

    # initial waktu_infeksi
    waktu_infeksi.append(0)

