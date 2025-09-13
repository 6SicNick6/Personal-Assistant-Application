from tkinter import *
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Tasks Program")

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    
    if task:
        with open("tasks.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)
        messagebox.showinfo(title="New task has been added", message="Succesfully added new task")

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        listbox.delete(ANCHOR)
        messagebox.showinfo(title="Task has been deleted", message="Succesfully deleted selected task")

def openTaskFile():
    try:
        global task_list
        with open("tasks.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        
        for task in tasks:
            if task !="\n":
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file = open("tasks.txt", "w")
        file.close()

input_frame = tk.Frame(window)
input_frame.pack(pady=10)

task_entry_label = tk.Label(input_frame, text="Add task:")
task_entry_label.grid(row=0, column=0, padx=5)

task_entry = tk.Entry(input_frame, width=30)
task_entry.grid(row=0, column=1, padx=5)

listbox_label = tk.Label(input_frame, text="The tasks you have:")
listbox_label.grid(row=1, column=0, padx=5, pady=50)

listbox = Listbox(input_frame, width=30, height=10)
listbox.grid(row=1, column=1, padx=5, pady=5)

scrollbar = Scrollbar(input_frame,orient="vertical")
scrollbar.grid(row=0,column=2,sticky='ns')
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command = listbox.yview)

add_button = tk.Button(window, text="Add task", command=addTask)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete task", command=deleteTask)
delete_button.pack(pady=5)

openTaskFile()

window.mainloop()