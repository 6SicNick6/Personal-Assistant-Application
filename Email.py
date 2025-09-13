import smtplib
import tkinter as tk
from tkinter import messagebox
import subprocess

window = tk.Tk()
window.title("Email Program")

def send_email():
    sender_email = sender_entry.get()
    sender_password = password_entry.get()
    receiver_email = receiver_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", "end")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(sender_email, sender_password)

            email_message = f"Subject: {subject}\n\n{message}"
            smtp.sendmail(sender_email, receiver_email, email_message)

        messagebox.showinfo("Success", "Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Authentication Error", "Failed to authenticate. Please check your email and password.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def receive_email():
    subprocess.call("C:/Program Files/Microsoft Office/root/Office16/OUTLOOK.EXE")

input_frame = tk.Frame(window)
input_frame.pack(pady=10)

sender_label = tk.Label(input_frame, text="Sender Email:")
sender_label.grid(row=0, column=0, padx=5)
sender_entry = tk.Entry(input_frame, width=30)
sender_entry.grid(row=0, column=1, padx=5)

password_label = tk.Label(input_frame, text="Password:")
password_label.grid(row=1, column=0, padx=5)
password_entry = tk.Entry(input_frame, width=30, show="*")
password_entry.grid(row=1, column=1, padx=5)

receiver_label = tk.Label(input_frame, text="Receiver Email:")
receiver_label.grid(row=2, column=0, padx=5)
receiver_entry = tk.Entry(input_frame, width=30)
receiver_entry.grid(row=2, column=1, padx=5)

subject_label = tk.Label(input_frame, text="Subject:")
subject_label.grid(row=3, column=0, padx=5)
subject_entry = tk.Entry(input_frame, width=30)
subject_entry.grid(row=3, column=1, padx=5)

message_label = tk.Label(input_frame, text="Message:")
message_label.grid(row=4, column=0, padx=5)
message_text = tk.Text(input_frame, width=30, height=10)
message_text.grid(row=4, column=1, padx=5)

send_button = tk.Button(window, text="Send Email", command=send_email)
send_button.pack(pady=5)

receive_button = tk.Button(window, text="Check Inbox", command=receive_email)
receive_button.pack(pady=5)

window.mainloop()