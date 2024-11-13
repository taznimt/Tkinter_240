 # Mengimpor modul tkinter, lalu memberi alias 'tk'
import tkinter as tk
#Mengimpor modul messagebox dari tkinter
from tkinter import messagebox

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    # Memulai blok try untuk menangani potensi kesalahan.
    try: 
        for entry in entries:
            nilai = int(entry.get())  # Berupa angka (int), jika tidak, maka akan terjadi ValueError.
            if not (0 <= nilai <= 100): # Bernilai antara 0 dan 100. Jika nilai di luar rentang tersebut, fungsi akan memunculkan ValueError.
                raise ValueError("Nilai harus antara 0 dan 100.")
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi") # Jika semua input valid, teks pada hasil_label diubah menjadi Prediksi Prodi Teknologi Informasi.
    except ValueError as ve:  # Jika ada kesalahan input, except menangkap ValueError dan menampilkan pesan error menggunakan messagebox.showerror.
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")


root = tk.Tk() #  membuat jendela utama untuk aplikasi.
root.title("Aplikasi Prediksi Prodi Pilihan") # memberi judul jendela aplikasi.
root.geometry("500x600")  # mengatur ukuran jendela aplikasi (lebar 500, tinggi 600 piksel).
root.configure(bg="#6a5acd") # mengatur warna latar belakang jendela utama.

# Label Judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#ee82ee") # Membuat label judul aplikasi
judul_label.pack(pady=20)  # Menempatkan label di jendela utama dengan padding vertikal

# Frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#6a5acd") # Membuat frame untuk mengelompokkan input nilai mata pelajaran
frame_input.pack(pady=10) # Menempatkan frame dengan padding vertikal 10 piksel

entries = [] # Membuat list kosong untuk menampung objek Entry
for i in range(10):  # Perulangan untuk membuat 10 pasangan Label dan Entry
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12), bg="#6a5acd")  # Membuat label untuk setiap mata pelajaran
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))  # Membuat entry untuk memasukkan nilai
    entry.grid(row=i, column=1, padx=10, pady=5)  # Menambahkan entry ke dalam list 'entries' agar bisa diakses nantinya
    entries.append(entry)


prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#4CAF50", fg="black")  # Tombol untuk menampilkan hasil prediksi
prediksi_button.pack(pady=30)

hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="purple", bg="#6a5acd") # Label untuk menampilkan hasil
hasil_label.pack(pady=20)

root.mainloop() # Memulai event loop Tkinter untuk menjalankan aplikasi


