# #input
# a = input("Masukan kalimat awal ; ")
# b = input("Masukan kata untuk disisipkan : ")
# c = int(input("Masukan index : "))


# def sisip():
#     jk = a.extend(c, b)
#     print(jk)

# sisip()
kalimat_awal = input("Masukan kalimat awal: ")
kata_sisipan = input("Masukan kata untuk disisipkan: ")
indeks = int(input("Masuka indeks: ")) - 1
hasil = f"{kalimat_awal[:indeks]}{kata_sisipan}{kalimat_awal[indeks:]}"
print(hasil)
