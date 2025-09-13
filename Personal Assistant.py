from tkinter import *
import subprocess

root = Tk()
root.title("Personal Assistant")
root.geometry("300x620")

def open_calendar():
    subprocess.run(["python", "Calendar.py"])

def open_contactbook():
    subprocess.run(["python", "contactlist/Contacts.py"])

def open_searcher():
    subprocess.run(["python", "Searcher.py"])

def open_weather():
    subprocess.run(["python", "Weather.py"])

def open_mail():
    subprocess.run(["python", "Email.py"])

def open_musicplayer():
    subprocess.run(["python", "Music.py"])

def open_alarm():
    subprocess.run(["python", "Alarm.py"])

def open_news():
    subprocess.run(["python", "News.py"])

def open_agenda():
    subprocess.run(["python", "Agenda.py"])

def open_textmsg():
    subprocess.run(["python", "Messages.py"])

def open_traffic():
    subprocess.run(["python", "Traffic.py"])
    
def open_caller():
    subprocess.run(["python", "Caller.py"])

def open_taskmanager():
    subprocess.run(["python", "tasklist/Tasks.py"])

intro = Label(root, text="Welcome to your personal assistant")
intro.grid(row=0, column=0, sticky=N)

calendar = Button(root, text="Calendar", command=open_calendar)
calendar.grid(row=1, column=0, pady=10, sticky=W)

contactbook = Button(root, text="Contacts", command=open_contactbook)
contactbook.grid(row=2, column=0, pady=10, sticky=W)

searcher = Button(root, text="Searcher", command=open_searcher)
searcher.grid(row=3, column=0, pady=10, sticky=W)

weather = Button(root, text="Weather", command=open_weather)
weather.grid(row=4, column=0, pady=10, sticky=W)

mail = Button(root, text="Email", command=open_mail)
mail.grid(row=5, column=0, pady=10, sticky=W)

music = Button(root, text="Music Player", command=open_musicplayer)
music.grid(row=6, column=0, pady=10, sticky=W)

alarm = Button(root, text="Notification", command=open_alarm)
alarm.grid(row=7, column=0, pady=10, sticky=W)

news = Button(root, text="News", command=open_news)
news.grid(row=8, column=0, pady=10, sticky=W)

agenda = Button(root, text="Agenda", command=open_agenda)
agenda.grid(row=9, column=0, pady=10, sticky=W)

msg = Button(root, text="Messages", command=open_textmsg)
msg.grid(row=10, column=0, pady=10, sticky=W)

traffic = Button(root, text="Traffic", command=open_traffic)
traffic.grid(row=11, column=0, pady=10, sticky=W)

caller = Button(root, text="Call", command=open_caller)
caller.grid(row=12, column=0, pady=10, sticky=W)

task = Button(root, text="Tasks", command=open_taskmanager)
task.grid(row=13, column=0, pady=10, sticky=W)

root.mainloop()