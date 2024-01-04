import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class BookingApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Aplikasi Booking Lapangan")
        self.label = tk.Label(text="Selamat Datang di Aplikasi Booking Lapangan", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)
        # Label
        self.label1 = tk.Label(window, text="Nama :")
        self.label1.grid(row=1, column=0)

        self.label2 = tk.Label(window, text="No Telp :")
        self.label2.grid(row=3, column=0)

        self.label3 = tk.Label(window, text="Tanggal :")
        self.label3.grid(row=5, column=0)

        self.label4 = tk.Label(window, text="Dari Jam :")
        self.label4.grid(row=7, column=0)

        self.label5 = tk.Label(window, text="Sampai Jam :")
        self.label5.grid(row=9, column=0)

        # Entry field
        self.entry_nama = tk.Entry(window, width=30)
        self.entry_nama.grid(row=1, column=1)

        self.entry_No = tk.Entry(window, width=30)
        self.entry_No.grid(row=3, column=1)

        self.entry_tanggal = tk.Entry(window, width=30)
        self.entry_tanggal.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.entry_tanggal.grid(row=5, column=1)

        # Dropdown menu for time selection
        self.time_var = tk.StringVar(window)
        self.time_var.set("09:00") 
        self.entry_jam = tk.OptionMenu(window, self.time_var, "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00")
        self.entry_jam.grid(row=7, column=1)

        # Dropdown menu for duration selection
        self.duration_var = tk.StringVar(window)
        self.duration_var.set("10:00") 
        self.entry_durasi = tk.OptionMenu(window, self.duration_var, "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00")
        self.entry_durasi.grid(row=9, column=1)

        # Button
        self.button = tk.Button(window, text="Pesan Lapangan", command=self.book, width=20)
        self.button.grid(row=11, column=1, pady=15)

        # History
        self.history_label = tk.Label(window, text="History:")
        self.history_label.grid(row=13, column=0)

        self.history_text = tk.Text(window, height=10, width=60)
        self.history_text.grid(row=15, column=0, columnspan=2)

        # Booking history
        self.booking_history = []

    def book(self):
        nama = self.entry_nama.get()
        tanggal = self.entry_tanggal.get()
        No = self.entry_No.get()
        jam = self.time_var.get()
        durasi = self.duration_var.get()
        booking_info = f"Nama: {nama}\nNo Telp: {No}\nTanggal: {tanggal}\nJam: {jam} - {durasi}"
        self.booking_history.append(booking_info)
        self.history_text.insert(tk.END, booking_info + "\n\n")
        messagebox.showinfo("Booking Info", f"Booking berhasil!\nNama: {nama}\nNo Telp: {No}\nTanggal: {tanggal}\nJam: {jam} - {durasi}")
