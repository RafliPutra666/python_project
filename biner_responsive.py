from tkinter import *

def on_resize(event):
    entry.config(width=event.width // 20)
    result_label.config(width=event.width // 10)
    button_biner.config(width=event.width // 30)
    button_desimal.config(width=event.width // 30)

root = Tk()
root.title("KALKULATOR BINER")
root.configure(bg="#728FCE")

Label(root, text="KALKULATOR BINER", font="calibri 14 bold", bg="#728FCE").grid(row=0, columnspan=2)

result_label = Label(root, font="calibri 15", fg="green", bg="#e0f7fa")
result_label.grid(row=3, pady=5, columnspan=2, sticky="nsew")  #responsivenya

def desimal():
    x = a.get()
    x = list(x)
    x = x[::-1]
    total = 0
    for index, bit in enumerate(x):
        total += int(bit) * (2 ** index)
    result_label.config(text=total)
    return total

def biner():
    x = a.get()
    x = int(x)
    bits = []
    while x > 0:
        bits.append(x % 2)
        x = x // 2
    bits = bits[::-1]
    result = ''.join(map(str, bits))
    result_label.config(text=result)
    return result

a = StringVar()
entry = Entry(root, textvariable=a, bg="#b3e0f2")
entry.grid(row=1, pady=5, columnspan=2, sticky="nsew")  # Menggunakan sticky agar responsive
entry.bind("<Configure>", on_resize)  # Menambahkan event handler untuk merespons perubahan ukuran

button_biner = Button(root, text="Ubah ke Biner", command=biner, bg="#151B54", fg="white")
button_biner.grid(row=2, column=0, sticky="nsew")  # Menggunakan sticky agar responsive

button_desimal = Button(root, text="Ubah ke Desimal", command=desimal, bg="#151B54", fg="white")
button_desimal.grid(row=2, column=1, sticky="nsew")  # Menggunakan sticky agar responsive

# biar kolom dan baris bisa ngisi ruang yang tersedia
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

root.mainloop()