import webbrowser
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("General Searcher")
root.geometry("300x50")

def searcher():
    webbrowser.open( "https://www.google.gr/search?q=" + searching.get())
    
def temp_text(e):
    search_entry.delete(0, "end")
   
searching = StringVar()

search_entry = Entry(root, textvariable=searching)
search_entry.insert(0, "Search Here...")
search_entry.pack()
search_entry.bind("<FocusIn>", temp_text)

search_button = Button(root, text="Search it", command=searcher)
search_button.pack()

root.mainloop()