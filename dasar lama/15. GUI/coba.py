import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.configure(bg="#8DF5A6")
window.geometry("300x200") # untuk mengatur ukuran
window.resizable() # untuk mengatur apakah ukuran windownya bisa di atur ata tidak
window.resizable(False,False) 
window.title("Sapa Dia!")

input_frame = ttk.Frame(window)
input_frame.pack(padx=10,pady=10,fill="x",expand=True)




window.mainloop()