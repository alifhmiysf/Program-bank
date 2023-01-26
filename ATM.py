# menyimpan saldo awal
saldo = 10000000000
# pin
pin = 9090
# penarikan
jumlah = 0
# setoran
setor = 0
# transfer
transfer = 0
# datetime
import datetime

# memilih bahasa
def bahasa():
    print("====================================")
    print("Pilih bahasa")
    print("1. Indonesia")
    print("2. English")
    print("====================================")
    pilih = int(input("Pilih bahasa: "))
    if pilih == 1:
        print("====================================")
        print("Selamat datang di ATM")
        print("Silahkan Masukkan PIN")
        pilih = int(input("Masukkan PIN: "))
        if pilih == pin:
            print("====================================")
            print("PIN benar")
            menu()
        else:
            print("====================================")
            print("PIN salah")
            print("Coba lagi")
            bahasa()
    elif pilih == 2:
        print("====================================")
        print("Welcome to ATM")
        print("Enter PIN")
        pilih = int(input("Enter PIN: "))
        if pilih == pin:
            print("====================================")
            print("PIN correct")
            menus()
        else:
            print("====================================")
            print("PIN wrong")
            print("Try again")
            bahasa()
    else:
        print("====================================")
        print("Pilihan tidak ada")
        bahasa()

# menu
def menu():
    print("====================================")
    print("Menu")
    print("1. Cek Saldo")
    print("2. Penarikan")
    print("3. Setor Tunai")
    print("4. Transfer")
    print("5. Keluar")
    pilih = int(input("Pilih menu: "))
    if pilih == 1:
        cek_saldo()
    elif pilih == 2:
        penarikan()
    elif pilih == 3:
        setor_tunai()
    elif pilih == 4:
        trans()
    elif pilih == 5:
        exit()
    else:
        print("====================================")
        print("Pilihan tidak ada")
        menu()

# saldo
def cek_saldo():
    print("====================================")
    print("Saldo Anda adalah Rp.", saldo)
    menu()

# penarikan
def penarikan():
    global datetime
    global saldo
    global jumlah
    print("====================================")
    print("Jumlah penarikan")
    print("1. Rp. 50.000")
    print("2. Rp. 100.000")
    print("3. Nominal lain")

    pilih = int(input("Pilih jumlah penarikan: "))
    if pilih == 1:
        jumlah = 50000
    elif pilih == 2:
        jumlah = 100000
    elif pilih == 3:
        print("====================================")
        print("Nominal lain")
        jumlah = int(input("Masukkan nominal: "))
    else:
        print("====================================")
        print("Pilihan tidak ada")
        penarikan()

    if jumlah > saldo:
        print("====================================")
        print("Saldo tidak cukup")
        penarikan()
    else:
        saldo = saldo - jumlah
        print("====================================")
        print("Struk")
        print("Hari:", datetime.datetime.now().strftime("%A"), ",", "Tanggal:", datetime.datetime.now().strftime("%d"), ",", "Bulan:", datetime.datetime.now().strftime("%B"), ",", "Tahun:", datetime.datetime.now().strftime("%Y"))
        print("Jam:", datetime.datetime.now().strftime("%H"),",", "Menit:", datetime.datetime.now().strftime("%M"), ",", "Detik:", datetime.datetime.now().strftime("%S"))
        print("====================================")
        print("Saldo awal: Rp.", saldo + jumlah)
        print("Penarikan: Rp.", jumlah)
        print("Saldo akhir: Rp.", saldo)
        menu()

# tunai
def setor_tunai():
    global datetime
    global saldo
    global setor
    print("====================================")
    print("Jumlah setoran")
    print("1. Rp. 50.000")
    print("2. Rp. 100.000")
    print("3. Nominal lain")

    pilih = int(input("Pilih jumlah setoran: "))
    if pilih == 1:
        setor = 50000
    elif pilih == 2:
        setor = 100000
    elif pilih == 3:
        print("====================================")
        print("Nominal lain")
        setor = int(input("Masukkan nominal: "))
    else:
        print("====================================")
        print("Pilihan tidak ada")
        setor_tunai()

    saldo = saldo + setor
    print("====================================")
    print("Struk")
    print("Hari:", datetime.datetime.now().strftime("%A"), ",", "Tanggal:", datetime.datetime.now().strftime("%d"), ",", "Bulan:", datetime.datetime.now().strftime("%B"), ",", "Tahun:", datetime.datetime.now().strftime("%Y"))
    print("Jam:", datetime.datetime.now().strftime("%H"),",", "Menit:", datetime.datetime.now().strftime("%M"), ",", "Detik:", datetime.datetime.now().strftime("%S"))
    print("====================================")
    print("Saldo awal: Rp.", saldo - setor)
    print("Setoran: Rp.", setor)
    print("Saldo akhir: Rp.", saldo)
    menu()

# transfer
def trans():
    global datetime
    global saldo
    global transfer
    print("====================================")
    rek = int(input("Masukkan nomor rekening: "))
    print("====================================")
    print("Jumlah transfer")
    print("1. Rp. 50.000")
    print("2. Rp. 100.000")
    print("3. Nominal lain")

    pilih = int(input("Pilih jumlah transfer: "))
    if pilih == 1:
        transfer = 50000
    elif pilih == 2:
        transfer = 100000
    elif pilih == 3:
        print("====================================")
        print("Nominal lain")
        transfer = int(input("Masukkan nominal: "))
    else:
        print("====================================")
        print("Pilihan tidak ada")

    if transfer > saldo:
        print("====================================")
        print("Saldo tidak cukup")

    else:
        saldo = saldo - transfer
        print("====================================")
        print("Struk")
        print("Hari:", datetime.datetime.now().strftime("%A"), ",", "Tanggal:", datetime.datetime.now().strftime("%d"), ",", "Bulan:", datetime.datetime.now().strftime("%B"), ",", "Tahun:", datetime.datetime.now().strftime("%Y"))
        print("Jam:", datetime.datetime.now().strftime("%H"),",", "Menit:", datetime.datetime.now().strftime("%M"), ",", "Detik:", datetime.datetime.now().strftime("%S"))
        print("====================================")
        print("Nomor rekening: ", rek)
        print("Saldo awal: Rp.", saldo + transfer)
        print("Transfer: Rp.", transfer)
        print("Saldo akhir: Rp.", saldo)
        menu()

# menu
def menus():
    print("====================================")
    print("Menu")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Cash Deposit")
    print("4. Transfer")
    print("5. Keluar")
    pilih = int(input("Chose Menu: "))
    if pilih == 1:
        cek_saldos()
    elif pilih == 2:
        penarikans()
    elif pilih == 3:
        setor_tunais()
    elif pilih == 4:
        transs()
    elif pilih == 5:
        exit()
    else:
        print("====================================")
        print("Chose not available")
        menus()

# saldo
def cek_saldos():
    print("====================================")
    print("Your Balance", saldo)
    menus()

# penarikan
def penarikans():
    global datetime
    global saldo
    global jumlah
    print("====================================")
    print("Withdraw amount")
    print("1. Rp. 50.000")
    print("2. Rp. 100.000")
    print("3. Other amount")

    pilih = int(input("Chose amount: "))
    if pilih == 1:
        jumlah = 50000
    elif pilih == 2:
        jumlah = 100000
    elif pilih == 3:
        print("====================================")
        print("Other amount")
        jumlah = int(input("Enter amount: "))
    else:
        print("====================================")
        print("Chose not available")
        penarikans()

    if jumlah > saldo:
        print("====================================")
        print("Insufficient balance")

    else:
        saldo = saldo - jumlah
        print("====================================")
        print("Receipt")
        print("Day:", datetime.datetime.now().strftime("%A"), ",", "Date:", datetime.datetime.now().strftime("%d"), ",", "Month:", datetime.datetime.now().strftime("%B"), ",", "Year:", datetime.datetime.now().strftime("%Y"))
        print("Hour:", datetime.datetime.now().strftime("%H"),",", "Minute:", datetime.datetime.now().strftime("%M"), ",", "Second:", datetime.datetime.now().strftime("%S"))
        print("====================================")
        print("Initial balance: Rp.", saldo + jumlah)
        print("Withdraw: Rp.", jumlah)
        print("Final balance: Rp.", saldo)
        menus()

# tunai
def setor_tunais():
    global datetime
    global saldo
    global setor
    print("====================================")
    print("Deposit amount")
    print("1. Rp. 50.000")
    print("2. Rp. 100.000")
    print("3. Other amount")

    pilih = int(input("Chose amount: "))
    if pilih == 1:
        setor = 50000
    elif pilih == 2:
        setor = 100000
    elif pilih == 3:
        print("====================================")
        print("Other amount")
        setor = int(input("Enter amount: "))
    else:
        print("====================================")
        print("Chose not available")
        setor_tunais()

    saldo = saldo + setor
    print("====================================")
    print("Receipt")
    print("Day:", datetime.datetime.now().strftime("%A"), ",", "Date:", datetime.datetime.now().strftime("%d"), ",", "Month:", datetime.datetime.now().strftime("%B"), ",", "Year:", datetime.datetime.now().strftime("%Y"))
    print("Hour:", datetime.datetime.now().strftime("%H"),",", "Minute:", datetime.datetime.now().strftime("%M"), ",", "Second:", datetime.datetime.now().strftime("%S"))
    print("====================================")
    print("Initial balance: Rp.", saldo - setor)
    print("Deposit: Rp.", setor)
    print("Final balance: Rp.", saldo)
    menus()

# transfer
def transs():
    global datetime
    global saldo
    global transfer
    print("====================================")
    reks = int(input("Enter account number: "))
    print("====================================")
    print("Transfer amount")
    print("1. Rp. 50.000")
    print("2. Rp. 100.000")
    print("3. Other amount")

    pilih = int(input("Chose amount: "))
    if pilih == 1:
        transfer = 50000
    elif pilih == 2:
        transfer = 100000
    elif pilih == 3:
        print("====================================")
        print("Other amount")
        transfer = int(input("Enter amount: "))
    else:
        print("====================================")
        print("Chose not available")
        transs()

    if transfer > saldo:
        print("====================================")
        print("Insufficient balance")

    else:
        saldo = saldo - transfer
        print("====================================")
        print("Receipt")
        print("Day:", datetime.datetime.now().strftime("%A"), ",", "Date:", datetime.datetime.now().strftime("%d"), ",", "Month:", datetime.datetime.now().strftime("%B"), ",", "Year:", datetime.datetime.now().strftime("%Y"))
        print("Hour:", datetime.datetime.now().strftime("%H"),",", "Minute:", datetime.datetime.now().strftime("%M"), ",", "Second:", datetime.datetime.now().strftime("%S"))
        print("====================================")
        print("Transfer To Account number:", reks)
        print("Initial balance: Rp.", saldo + transfer)
        print("Transfer: Rp.", transfer)
        print("Final balance: Rp.", saldo)
        menus()

def exit():
    print("====================================")
    print("Thank you")

# memanggil fungsi bahasa
bahasa()