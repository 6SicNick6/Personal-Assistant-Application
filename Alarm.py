import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import time
from plyer import notification

def set_alarm():
    try:
        hour = int(hour_entry.get())
        minute = int(minute_entry.get())
        am_pm = am_pm_combobox.get()
        
        if am_pm == 'PM' and hour != 12:
            hour += 12
        elif am_pm == 'AM' and hour == 12:
            hour = 0
        
        current_time = datetime.now().strftime("%H:%M")
        alarm_time = f"{hour:02d}:{minute:02d}"
        
        if current_time == alarm_time:
            show_notification()
            return
        
        while current_time != alarm_time:
            time.sleep(1)
            current_time = datetime.now().strftime("%H:%M")
        
        show_notification()
    except ValueError:
        messagebox.showerror("Error", "Please enter valid time values.")

def show_notification():
    title = "Alarm Notification"
    message = "Time's up!"
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

window = tk.Tk()
window.title("Alarm App")

input_frame = ttk.Frame(window)
input_frame.pack(pady=10)

hour_label = ttk.Label(input_frame, text="Hour:")
hour_label.grid(row=0, column=0, padx=5)
hour_entry = ttk.Entry(input_frame, width=5)
hour_entry.grid(row=0, column=1, padx=5)

minute_label = ttk.Label(input_frame, text="Minute:")
minute_label.grid(row=0, column=2, padx=5)
minute_entry = ttk.Entry(input_frame, width=5)
minute_entry.grid(row=0, column=3, padx=5)

am_pm_label = ttk.Label(input_frame, text="AM/PM:")
am_pm_label.grid(row=0, column=4, padx=5)
am_pm_combobox = ttk.Combobox(input_frame, values=['AM', 'PM'], width=3)
am_pm_combobox.grid(row=0, column=5, padx=5)
am_pm_combobox.current(0)

set_alarm_button = ttk.Button(window, text="Set Alarm", command=set_alarm)
set_alarm_button.pack(pady=5)

window.mainloop()