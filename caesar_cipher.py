# Caesar Cipher Encryption
# https://en.wikipedia.org/wiki/Caesar_cipher

import tkinter as tk
from tkinter import messagebox as msg
from ceaser import Ceaser

FONT = ("Arial", 14, "bold")
form = tk.Tk()
form.title("Caesar Cipher")
form.minsize(width=700, height=450)

lblTitle = tk.Label(form, text="Caesar Cipher Encryption")
lblTitle.config(font=("Arial", 18, "bold"))
lblTitle.pack(pady=15)

lblMessage = tk.Label(form, text="Message", font=FONT)
lblMessage.pack()
lblMessage.place(relx=0.08, rely=0.15)

txtMessage = tk.Text(form, width=20, height=10, font=FONT)
txtMessage.pack()
txtMessage.place(relx=0.05, rely=0.22)

lblResult = tk.Label(form, text="Result", font=FONT)
lblResult.pack()
lblResult.place(relx=0.7, rely=0.15)

txtResult = tk.Text(form, width=20, height=10, font=FONT)
txtResult.pack()
txtResult.place(relx=0.65, rely=0.22)

lblShiftKey = tk.Label(form, text="Key", font=FONT)
lblShiftKey.pack()
lblShiftKey.place(relx=0.4, rely=0.22)

varShiftKey = tk.IntVar(value=5)
sbKey = tk.Spinbox(form, from_=1, to=26, width=5,
                   font=FONT, textvariable=varShiftKey)
sbKey.pack()
sbKey.place(relx=0.47, rely=0.22)


def msgEncrypt():
    try:
        shiftKey = varShiftKey.get()
        message = txtMessage.get("1.0", tk.END).strip()
        c = Ceaser(shiftKey)
        encrypted_message = c.EncryptMessage(message)
        txtResult.delete("1.0", tk.END)
        txtResult.insert("1.0", encrypted_message)
        msg.showinfo("Caesar Cipher", "Message encrypted successfully!")
    except Exception as ex:
        msg.showerror("Caesar Cipher", ex)


def msgDecrypt():
    try:
        shiftKey = varShiftKey.get()
        message = txtMessage.get("1.0", tk.END).strip()
        c = Ceaser(shiftKey)
        encrypted_message = c.DecryptMessage(message)
        txtResult.delete("1.0", tk.END)
        txtResult.insert("1.0", encrypted_message)
        msg.showinfo("Caesar Cipher", "Message decrypted successfully!")
    except Exception as ex:
        msg.showerror("Caesar Cipher", ex)


btnEncrypt = tk.Button(form, font=FONT, text="Encrypt",
                       width=12, command=msgEncrypt)
btnEncrypt.pack()
btnEncrypt.place(relx=0.40, rely=0.37)

btnDecrypt = tk.Button(form, font=FONT, text="Decrypt",
                       width=12, command=msgDecrypt)
btnDecrypt.pack()
btnDecrypt.place(relx=0.40, rely=0.52)

form.mainloop()
