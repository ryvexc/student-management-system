from colorama import Style
from tools import *
from conf import *

def clear_data() -> None:
    with open("local/data.db", "w") as local_data:
        local_data.write("")
        local_data.close()

def write_data(data: str, appendNewLine: bool = True) -> None:
    with open("local/data.db", "a+") as local_data:
        local_data.write(f"{data}\n")
        local_data.close()

def get_data() -> list:
    with open("local/data.db", "r") as local_data:
        return [data for data in local_data.readlines()]

class Highest:
    nama: int = 0
    kelas: int = 0
    asal_sekolah: int = 0
    kota: int = 0
    provinsi: int = 0

def print_data(data_get: list = [], header_name: str = "", number_id: int = -1) -> None:
    data_get = data_get if data_get != [] else get_data()
    # mengambil panjang kalimat tertinggi
    for data in data_get: # data -> str
        s_data = data.split(",")
        Highest.nama = len(s_data[0]) if len(s_data[0]) > Highest.nama else Highest.nama
        Highest.kelas = len(s_data[1]) if len(s_data[1]) > Highest.kelas else Highest.kelas
        Highest.asal_sekolah = len(s_data[2]) if len(s_data[2]) > Highest.asal_sekolah else Highest.asal_sekolah
        Highest.kota = len(s_data[3]) if len(s_data[3]) > Highest.kota else Highest.kota
        Highest.provinsi = len(s_data[4]) - 1 if len(s_data[4]) > Highest.provinsi else Highest.provinsi

    # "| nama | kelas | asal sekolah | kota | provinsi |"
    PANJANG_GARIS = (
        len(str(len(data_get))) + (1 if len(str(len(data_get))) >= 2 else 2)+
        2+(Highest.nama if Highest.nama >= 4 else 4)+
        3+(Highest.kelas if Highest.kelas >= 5 else 5)+
        3+(Highest.asal_sekolah if Highest.asal_sekolah >= 12 else 12)+
        3+(Highest.kota if Highest.kota >= 4 else 4)+
        3+(Highest.provinsi if Highest.provinsi >= 8 else 8)+2
    )

    # print header
    if header_name != "":
        print_garis(PANJANG_GARIS)
        print("| " + HEADER_COLOR + header_name, end="")
        print_white_space(PANJANG_GARIS - (4 + len(header_name)))
        print(Fore.WHITE + " |")

    # print subheader
    print_garis(PANJANG_GARIS)
    print(f"| {Fore.LIGHTRED_EX}No{Fore.WHITE}", end="")
    print_white_space(1 if len(str(len(data_get))) + 1 <= 2 else len(str(len(data_get))) + 1 - 2)
    print(f"| {Fore.LIGHTRED_EX}Nama{Fore.WHITE}", end="")
    print_white_space(1 if Highest.nama <= 4 else Highest.nama - 3)
    print(f"| {Fore.LIGHTRED_EX}Kelas{Fore.WHITE}", end="")
    print_white_space(1 if Highest.kelas <= 5 else Highest.kelas - 5)
    print(f"| {Fore.LIGHTRED_EX}Asal Sekolah{Fore.WHITE}", end="")
    print_white_space(1 if Highest.asal_sekolah <= 12 else Highest.asal_sekolah - 12)
    print(f"| {Fore.LIGHTRED_EX}Kota{Fore.WHITE}", end="")
    print_white_space(1 if Highest.kota <= 4 else Highest.kota - 4)
    print(f"| {Fore.LIGHTRED_EX}Provinsi{Fore.WHITE}", end="")
    print_white_space(1 if Highest.provinsi <= 8 else Highest.provinsi - 8)
    print("|"+Fore.WHITE)
    print_garis(PANJANG_GARIS)

    # print data
    for i in range(len(data_get)):
        s_data = data_get[i].split(",")
        print(f"| {Fore.LIGHTBLUE_EX}{i+1 if number_id == -1 else number_id}{Fore.WHITE}", end="")
        print_white_space(len(str(len(data_get))) - len(str(i+1)) + (1 if len(str(len(data_get))) >= 2 else 2))
        print("| "+s_data[0], end="")
        print_white_space(5 - len(s_data[0]) if Highest.nama <= 4 else Highest.nama - len(s_data[0]) + 1)
        print("| "+s_data[1][1:], end="")
        print_white_space(6 - len(s_data[1]) + 1 if Highest.kelas <= 5 else Highest.kelas - len(s_data[1]) + 1)
        print("| "+s_data[2][1:], end="")
        print_white_space(13 - len(s_data[2]) + 1 if Highest.asal_sekolah <= 12 else Highest.asal_sekolah - len(s_data[2]) + 1)
        print("| "+s_data[3][1:], end="")
        print_white_space(5 - len(s_data[3]) + 1 if Highest.kota <= 4 else Highest.kota - len(s_data[3]) + 1)
        print("| "+s_data[4][1:-1], end="")
        print_white_space(9 - len(s_data[4]) + 2 if Highest.provinsi <= 9 else Highest.provinsi - len(s_data[4]) + 2)
        print("|")

    print_garis(PANJANG_GARIS)

if __name__ == '__main__':
    print_data(header_name="RYVE GG")