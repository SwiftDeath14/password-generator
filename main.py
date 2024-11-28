'''
Password Generator
-------------------------------------------------------------
Program ini digunakan untuk membuat password yang aman dan kuat. 
Password akan terdiri dari huruf, angka, dan karakter spesial.
'''
import secrets  # Pustaka untuk menghasilkan angka acak yang aman
import string  # Pustaka untuk menyediakan kumpulan huruf, angka, dan simbol

# Fungsi untuk membuat password
def create_pw(pw_length=12):
    # Menggabungkan huruf kecil, huruf besar, angka, dan karakter spesial
    letters = string.ascii_letters  # Semua huruf (A-Z dan a-z)
    digits = string.digits  # Semua angka (0-9)
    special_chars = string.punctuation  # Semua karakter spesial (!, @, #, dll)

    alphabet = letters + digits + special_chars  # Gabungan semua karakter
    pwd = ''  # Variabel untuk menyimpan password
    pw_strong = False  # Variabel untuk memastikan password kuat

    while not pw_strong:
        pwd = ''  # Reset password setiap iterasi
        for i in range(pw_length):
            # Menambahkan karakter acak dari kumpulan alfabet
            pwd += ''.join(secrets.choice(alphabet))

        # Memastikan password mengandung minimal 1 karakter spesial dan 2 angka
        if (any(char in special_chars for char in pwd) and
                sum(char in digits for char in pwd) >= 2):
            pw_strong = True  # Password dianggap kuat jika memenuhi syarat

    return pwd  # Mengembalikan password yang dihasilkan

# Program utama
if __name__ == '__main__':
    # Menampilkan password yang dihasilkan ke layar
    print(create_pw())
