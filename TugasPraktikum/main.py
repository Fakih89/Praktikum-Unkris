from datetime import datetime
print("#"*50)
print("\t\tKANTIN KEJUJURAN")
print("#"*50)
print("\t\tDAFTAR MENU")
kebab = ["Kebab Mini Rp. 8.000","Kebab Small Rp. 10.000","Kebab Medium Rp. 15.000","Kebab Large Rp. 18.000"]
hotdog = ["Hotdog Ori  Rp. 15.000", "Hotdog Black Rp. 16.000"]
burger = ["Burger Ori Rp. 14.000","Black Burger Rp. 14.000","Double Burger Ori Rp. 20.000","Double Burger Black Rp. 20.000","Burger Ayam Rp. 15.000","Burger Kebab Rp. 14.000"]
print("Kebab:")
for i in kebab:
    print(i)
print("\nHotdog:")
for i in hotdog:
    print(i)
print("\nBurger:")
for i in burger:
    print(i)
print("\n"+"#"*50)
nama = input("Nama Pelanggan :")
alamat = input("Alamat :")
no_telp = input("No Telp :")
tanggal = datetime.now().strftime('%w %B %Y')
total = 0
barang = []
while True:
    menu = input("Pilih Menu :").lower()
    jumlah = int(input("Jumlah :"))
    match menu:
        case "kebab mini":harga = 8000 ,barang.append(menu)
        case "kebab small":harga = 10000,barang.append(menu)
        case "kebab medium":harga = 15000,barang.append(menu)
        case "kebab large":harga = 18000,barang.append(menu)
        case "hotdog ori":harga = 15000,barang.append(menu)
        case "hotdog black":harga = 16000,barang.append(menu)
        case "burger ori":harga = 14000,barang.append(menu)
        case "black burger":harga = 14000,barang.append(menu)
        case "double burger ori":harga = 20000,barang.append(menu)
        case "double burger black":harga = 20000,barang.append(menu)
        case "burger ayam":harga = 15000,barang.append(menu)
        case "burger kebab":harga = 14000,barang.append(menu)
        case _:harga = 0,print("Pilihan Tidak ada")
    total = total + (harga[0]*jumlah)
    more = input("Apakah ada pesanan lagi? ")
    if more == "iya" or more == "ya" or more == "y":
        continue
    else:
        break
print("#"*50)
print("Nama Pelanggan : {}".format(nama))
print("Alamat : {}".format(alamat))
print("No Telp : {}".format(no_telp))
print("Tanggal : {}".format(tanggal))
print("Barang Pesanan:\n#")
n = 0
for i in barang:
    n+=1
    print("{}. {}".format(n,i))
print("#")
print("Total Harga = {}".format(total))