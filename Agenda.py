import tkinter as tk
from tkinter import messagebox
from datetime import date

root = tk.Tk()

class Appointment:
    def __init__(self, title, date):
        self.title = title
        self.date = date

class CalendarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Appointment Manager")

        self.calendar_frame = tk.Frame(self.root)
        self.calendar_frame.pack(pady=10)

        self.title_label = tk.Label(self.calendar_frame, text="Appointments", font=("Helvetica", 16, "bold"))
        self.title_label.pack()

        self.appointments_listbox = tk.Listbox(self.calendar_frame, width=50, height=10, font=("Helvetica", 12))
        self.appointments_listbox.pack(pady=10)

        self.add_button = tk.Button(self.calendar_frame, text="Add Appointment", command=self.open_add_appointment)
        self.add_button.pack(pady=10)

        self.delete_button = tk.Button(self.calendar_frame, text="Delete Appointment", command=self.delete_appointment)
        self.delete_button.pack(pady=5)

        self.appointments = []

    def open_add_appointment(self):
        self.add_window = tk.Toplevel()
        self.add_window.title("Add Appointment")

        self.title_label = tk.Label(self.add_window, text="Title:")
        self.title_label.grid(row=0, column=0, padx=10, pady=10)
        self.title_entry = tk.Entry(self.add_window, font=("Helvetica", 12))
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)

        self.date_label = tk.Label(self.add_window, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=1, column=0, padx=10, pady=10)
        self.date_entry = tk.Entry(self.add_window, font=("Helvetica", 12))
        self.date_entry.grid(row=1, column=1, padx=10, pady=10)

        self.add_button = tk.Button(self.add_window, text="Add", command=self.add_appointment)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def add_appointment(self):
        title = self.title_entry.get()
        date_str = self.date_entry.get()

        if not title or not date_str:
            messagebox.showerror("Error", "Please enter a title and a date.")
            return

        try:
            date_obj = date.fromisoformat(date_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
            return

        appointment = Appointment(title, date_obj)
        self.appointments.append(appointment)
        self.appointments_listbox.insert(tk.END, f"{appointment.title} - {appointment.date}")

        self.add_window.destroy()

    def delete_appointment(self):
        selected_index = self.appointments_listbox.curselection()
        if not selected_index:
            return
        appointment = self.appointments[selected_index[0]]
        confirm = messagebox.askyesno("Delete Appointment", f"Are you sure you want to delete the appointment:\n\n{appointment.title} - {appointment.date}?")
        if confirm:
            self.appointments.pop(selected_index[0])
            self.appointments_listbox.delete(selected_index)

calendar_gui = CalendarGUI(root)
root.mainloop()
