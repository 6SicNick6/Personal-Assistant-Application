from twilio.rest import Client
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Send Messages")

account_sid = "AC253eae7ac65206cfae3ff8917183f400"
auth_tonken = "b03f764243bba9c5459df9f547519750"

twilio_number = "+12342901832"

def send_message():
    client = Client(account_sid, auth_tonken)
    
    message = client.messages.create(
        body= message_text.get("1.0", "end"),
        from_= twilio_number,
        to="+30" + target_number.get()
    )

input_frame = tk.Frame(window)
input_frame.pack(pady=10)

target_number_label = tk.Label(input_frame, text="Target Number:")
target_number_label.grid(row=0, column=0, padx=5)

target_number = tk.Entry(input_frame, width=30)
target_number.grid(row=0, column=1, padx=5)

message_label = tk.Label(input_frame, text="Message:")
message_label.grid(row=1, column=0, padx=5)

message_text = tk.Text(input_frame, width=30, height=10)
message_text.grid(row=1, column=1, padx=5)

send_button = tk.Button(window, text="Send message", command=send_message)
send_button.pack(pady=30)

window.mainloop()
