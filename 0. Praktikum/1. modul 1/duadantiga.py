def matrik():
    baris = int(input("Jumlah Baris = "))
    kolom = int(input("Jumlah Kolom = "))
    matrik = []

    for a in range(baris):
        matrik_baris = []
        for b in range(kolom):
            matrik_baris.append(0)
        matrik.append(matrik_baris)

    total_inp = int(input("Jumlah Data = "))
    while total_inp > 0:
        baris_ke = int(input("Baris ke ? "))
        kolom_ke = int(input("Kolom ke ? "))
        data_yg_diubah = int(input("matrik[{0}][{1}]= ".format(baris_ke, kolom_ke)))
        matrik[baris_ke][kolom_ke] = data_yg_diubah

        total_inp = total_inp - 1

    return matrik


def tampilan(matrik):
    baris = len(matrik)
    kolom = len(matrik[0])

    for a in range(baris):
        for b in range(kolom):
            print(matrik[a][b], end=" ")
        print("")


def perkalian(matrik1, matrik2):
    matrik = []

    
    if len(matrik1[0]) == len(matrik2):
        for a in range(len(matrik1)):
            data = []
            for b in range(len(matrik2[0])):
                hasil = 0
                for c in range(len(matrik1[0])):
                    hasil = hasil + matrik1[a][c] * matrik2[c][b]
                data.append(hasil)
            matrik.append(data)
    else:
        print("Matrik Tersebut Tidak Bisa Dikali")

    
    for baris in range(len(matrik)):
        for kolom in range(len(matrik[0])):
            print(matrik[baris][kolom], end=" ")
        print("")
