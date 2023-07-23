# GUI -> Graphical User Interface

# biasahnya progam akan berjalan looping terus menerus sampai kita keluar dengan tombol X

import tkinter as tk
from tkinter import ttk # untuk mengatur posisi item yang ada di dalam window (frame)
from tkinter.messagebox import showinfo # untuk menampilkan pop up window

# Init
window = tk.Tk() # membuat tampilan awal atau app/window
window.configure(bg="white") # bisa untuk mengatur selain warna (untuk warna bisa menggnakan nilai hexadesimal dari suatu warna)
window.geometry("500x500") # untuk mengatur ukuran
window.resizable(False,False) # untuk mengatur apakah ukuran windownya bisa di atur atau tidak, false = tidak, true = bisa
             # lebar, tinggi
window.title("Sapa Dia!") # untuk judul yang di tampilkan di window

# Variabel dan Fungsi
NAMA_DEPAN = tk.StringVar() # untuk menangkap nilai inputan dan merubahnya menjadi string
NAMA_BELAKANG = tk.StringVar() # untuk menangkap nilai inputan dan merubahnya menjadi string

def tombol_click():
    '''fungsi ini akan dipanggil oleh tombol'''
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Ganteeeng!"
    showinfo(title="Whazzup!",message=pesan)

# frame input
input_frame = ttk.Frame(window) # untuk membri frame dalam window
# penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True,) # membuat ukuran frame
               # panding/batas , sumbu x(kesamping), posisi tengah (true)

# komponen-komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan:")
nama_depan_label.pack(padx=10,fill="x",expand=True) # pack untuk menampilkan (contoh gampangnya seperti print())
# 2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)
# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama belakang:")
nama_belakang_label.pack(padx=10,fill="x",expand=True)
# 4. entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)
# 5. Tombol
tombol_sapa = ttk.Button(input_frame,text="Sapa!",command=tombol_click)
tombol_sapa.pack(fill='x',expand=True,padx=10,pady=10)

# Main Loop window
window.mainloop() # agar progam berjalan / tampil