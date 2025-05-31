from tkinter import *
from tkinter import messagebox
import base64

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def save_and_encrypt_notes():
    title = enter_title_input.get()
    massage = enter_secret_text.get("1.0", END)
    master_secret = enter_masterkey_input.get()

    if len(title) == 0 or len(massage) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title= "Error", message="Please fill all fields")
    else:

        massage_encrypted = encode(master_secret, massage)
        try:
            with open("mysecret.txt", "a") as data_file:
                data_file.write(f"\n{title}\n{massage_encrypted}")
        except FileNotFoundError:
            with open("mysecret.txt", "w") as data_file:
                    data_file.write(f"\n{title}\n{massage_encrypted}")
        finally:
            enter_title_input.delete(0, END)
            enter_secret_text.delete(0.0, END)
            enter_masterkey_input.delete(0, END)

def decrypt_notes():
    message_encrypted = enter_secret_text.get("1.0", END)
    master_secret = enter_masterkey_input.get()

    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title= "Error", message="Please fill all fields")
    else:
        try:
            decrypted_message = decode(master_secret, message_encrypted)
            enter_secret_text.delete("1.0", END)
            enter_secret_text.insert("1.0", decrypted_message)
        except:
            messagebox.showinfo(title= "Error", message="Please enter encrypted text!")


window = Tk()
window.title("Secret Note App")
window.minsize(width=400, height=700)
window.config(padx=20, pady=20)
FONT = ("Verdena", 10, "bold")

photo = PhotoImage(file=".venv/Scripts/secretnote.png")
photo_label = Label(image=photo)
photo_label.pack()

enter_title = Label(text="Enter your title" , font=FONT)
enter_title.config(padx=20, pady=20)
enter_title.pack()

enter_title_input = Entry(width=30)
enter_title_input.pack()
enter_title_input.focus()

enter_secret = Label(text="Enter your secret" , font=FONT)
enter_secret.config(padx=20, pady=20)
enter_secret.pack()

enter_secret_text = Text(width=30, height=15)
enter_secret_text.config(padx=20, pady=20)
enter_secret_text.pack()

enter_masterkey = Label(text="Enter master key" , font=FONT)
enter_masterkey.config(padx=20, pady=20)
enter_masterkey.pack()

enter_masterkey_input = Entry(width=30)
enter_masterkey_input.config(show="*")
enter_masterkey_input.pack()

save_button = Button(text="Save & Encrypt", command=save_and_encrypt_notes)
save_button.pack()

descrypt_button = Button(text="Decrypt", command=decrypt_notes)
descrypt_button.pack()

window.mainloop()