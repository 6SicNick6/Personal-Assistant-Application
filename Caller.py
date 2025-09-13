from twilio.rest import Client
import tkinter as tk

window = tk.Tk()
window.title("Call someone")

account_sid = "AC253eae7ac65206cfae3ff8917183f400"
auth_tonken = "b03f764243bba9c5459df9f547519750"

twilio_number = "+12342901832"

def call():
    client = Client(account_sid, auth_tonken)

    call = client.calls.create(twiml="<Response><Say>Testing call api by Siolas</Say></Response>",
                           to="+30"+ target_number.get(),
                           from_= twilio_number)

    print(call.sid)

input_frame = tk.Frame(window)
input_frame.pack(pady=10)

target_number_label = tk.Label(input_frame, text="Target Number:")
target_number_label.grid(row=0, column=0, padx=5)

target_number = tk.Entry(input_frame, width=30)
target_number.grid(row=0, column=1, padx=5)

send_button = tk.Button(window, text="call him!", command=call)
send_button.pack(pady=5)

window.mainloop()