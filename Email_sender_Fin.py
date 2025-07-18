import tkinter as tk
from tkinter import ttk

from email.message import EmailMessage
import ssl
import smtplib


root = tk.Tk()
root.title("Email Sender Application")  
root.geometry("700x700")  
root.resizable(False, False)  # Prevents resizing

style = ttk.Style()
style.theme_use("clam")  

header = tk.Frame(root, bg="lightblue", height=50)
header.pack(fill="x")
header.pack_propagate(False)  # Ensure height stays fixed

label = ttk.Label(header, text="Message Center", font=("Arial", 16))
label.pack(pady=10)

Sender_label = ttk.Label(root, text="Enter Receiver Email:", font=("Arial", 13))
Sender_label.pack(pady=12)  

Sender_entry = tk.Entry(root,width=40)
Sender_entry.pack(pady=5)  

subject_label = ttk.Label(root, text="Enter Subject Line:", font=("Arial", 13))
subject_label.pack(pady=12)  
 
entry = tk.Entry(root,width=40)
entry.pack(pady=5)   
 
body_label = ttk.Label(root, text="Enter Email body:", font=("Arial", 13))
body_label.pack(pady=12)  

entry2 = tk.Text(root, height=19, width=75)  # Directly controls height
entry2.pack(pady=10)

def send_mess():
    notif_label.config(text="Message Sent")
    
    sender = 'sarmientomark3663@gmail.com'
    email_password = 'qcnx ejcf edqn vfsd'
    receiver = Sender_entry.get().strip()

        
    subject = entry.get().strip()
    body = entry2.get("1.0", "end-1c")

    em = EmailMessage()
    em['From'] = sender
    em['To'] = receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
        smtp.login(sender,email_password)
        smtp.sendmail(sender,receiver,em.as_string())





button = ttk.Button(root, text="Submit Message!", command=send_mess)
button.pack(pady=10)

notif_label = ttk.Label(root, text="", font=("Arial", 13),bg=None)
notif_label.pack(pady=3)

root.mainloop()
