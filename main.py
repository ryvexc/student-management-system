import os
from tools import *
from data_manager import *

WELCOME = "Welcome to Student Management!"

def show_menu() -> None:
    menus: list = ["Insert data", "Remove data", "View data"]
    print(f"| {NUMBER_COLOR}0.{Fore.RED} Keluar{Fore.WHITE}", end="")
    print_white_space(len(WELCOME) - len("| 0. Keluar") + 3)
    print("|")
    for i in range(len(menus)):
        print(f"| {NUMBER_COLOR}{i+1}. {Fore.WHITE}{menus[i]}", end="")
        print_white_space(len(WELCOME) - len(f"| {i+1}. {menus[i]}") + 3)
        print("|")

def insert_data() -> None:
    while True:
        os.system("cls")
        print(f"{Fore.WHITE}Masukkan data dengan tepat!, ketik '{IMPORTANT_COLOR}-BACK-{Fore.WHITE}' untuk kembali!")
        nama = str(input(f"{Fore.WHITE}Nama: {INPUT_COLOR}"))
        if nama == "-BACK-":
            break
        nama = nama.title()
        kelas = int(input(f"{Fore.WHITE}Kelas: {INPUT_COLOR}"))
        asal_sekolah = str(input(f"{Fore.WHITE}Asal sekolah: {INPUT_COLOR}")).capitalize()
        kota = str(input(f"{Fore.WHITE}Kota: {INPUT_COLOR}")).title()
        provinsi = str(input(f"{Fore.WHITE}Provinsi: {INPUT_COLOR}")).title()

        formatted_user_input = f"{nama}, {kelas}, {asal_sekolah}, {kota}, {provinsi}"

        # Check kalo ada data yang sama
        data_get = get_data()
        data_sama = False
        for data in data_get:
            s_data = data.split(",")

            # DEBUG
            # for i in range(len(s_data)):
            #     if i == len(s_data) - 1: print(f"data check {i}: {s_data[i][1:-1]}, len: {s_data[i][1:-1].__len__()}")
            #     else: 
            #         if i == 0: print(f"data check {i}: {s_data[i]}, len: {s_data[i].__len__()}")
            #         else: print(f"data check {i}: {s_data[i][1:]}, len: {s_data[i][1:].__len__()}")

            if s_data[0] == nama and int(s_data[1][1:]) == kelas and s_data[2][1:] == asal_sekolah and s_data[3][1:] == kota and s_data[4][1:-1] == provinsi:
                print(f"{WARNING_COLOR}Data telah tersedia, {ERROR_COLOR}data gagal ditambahkan!{Fore.WHITE}")
                data_sama = True
                break

        if not data_sama: 
            write_data(formatted_user_input)
            print(f"{SUCCESS_COLOR}Data telah ditambahkan")
        if input(f"\n{PROMPT_COLOR}Apakah anda ingin menambahkan data {'baru' if not data_sama else 'yang lain'}? [y/n]: {Fore.WHITE}") == "n":
            break

def remove_data() -> None:
    while True:
        os.system("cls")
        data_get = get_data()
        print(Fore.WHITE)
        
        # Nampilin data yang ada di database
        print_data(header_name="Data Ditemukan")

        # menghapus data yang dipilih
        urutan_data_terpilih = int(input(IMPORTANT_COLOR+"Ketik 0 untuk kembali"+PROMPT_COLOR+"\nPilihan> "+NUMBER_COLOR))
        if urutan_data_terpilih == 0:
            break
        print(Fore.WHITE)
        print_data(data_get=[data_get[urutan_data_terpilih - 1]], number_id=urutan_data_terpilih)
        if input(PROMPT_COLOR+ "Apakah anda yakin akan menghapus data tersebut? [y/n]: " + YES_OR_NO_COLOR) == "y":
            # proses hapus data lokal
            selected_data: list = []
            for data in data_get:
                if data == data_get[urutan_data_terpilih - 1]:
                    continue
                selected_data.append(data)

            # menulis ulang data ke database lokal
            clear_data()
            [write_data(data[:-1]) for data in selected_data]
            print(f"{SUCCESS_COLOR}Data telah terhapus!{Fore.WHITE}")
        else:
            print(SUCCESS_COLOR+"Penghapusan dibatalkan."+Fore.WHITE)
        if input(f"\n{PROMPT_COLOR}Apakah anda ingin menghapus data lainnnya? [y/n]: {YES_OR_NO_COLOR}") == "n":
            break

def view_data() -> None:
    while True:
        print(Fore.WHITE)
        os.system("cls")
        data_get = get_data()
        if len(data_get) != 0: 
            print_data(header_name="Data Tersedia")
        else:
            print("Data kosong!")

        if input(PROMPT_COLOR+"kemabali ke menu? [y/n]: "+YES_OR_NO_COLOR) == "y":
            break

def process_user_input(inp: int) -> None:
    os.system("cls")
    if inp == 0 or inp == 99:
        print(Fore.WHITE)
        exit(0)
    elif inp == 1: insert_data()
    elif inp == 2: remove_data()
    elif inp == 3: view_data()
    else: print("input salah!")

if __name__ == '__main__':
    while True:
        print(Fore.WHITE)
        os.system("cls")
        print_garis(len(WELCOME) + 4)
        print(f"| {HEADER_COLOR}{WELCOME}{Fore.WHITE} |")
        print_garis(len(WELCOME) + 4)
        show_menu()
        print_garis(len(WELCOME) + 4)
        process_user_input(int(input(PROMPT_COLOR+"Opsi> "+NUMBER_COLOR)))
    
    