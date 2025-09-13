from tkinter import *
from tkcalendar import *
from tkinter import messagebox
from datetime import date

root = Tk()
root.title("Calendar")
root.geometry("600x400")

cal = Calendar(root, selectmode="day", year=2023, month=7, day=14)
cal.pack(pady=20, fill="both", expand="true")

today = date.today()

def grab_date():
    messagebox.showinfo("What's today's date?", "Today's date is " + str(today))

my_button = Button(root, text="What's today's date?", command=grab_date)
my_button.pack(pady=20)

root.mainloop()