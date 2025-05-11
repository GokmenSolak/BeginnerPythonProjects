from tkinter import *

window = Tk()
window.title("Widget Examples")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

#label
my_label = Label(text="This is my label", font=("Arial", 11, "bold"))
my_label.config(bg="black", fg="white")
my_label.config(padx=10, pady=10)
my_label.pack()

#button
def button_clicked():
    print("I clicked the button!")
    print(my_text.get("2.0", END))

my_button = Button(text="Click Me!", command=button_clicked)
my_button.config(padx=10, pady=10)
my_button.pack()

#entry
my_entry = Entry(width=30)
my_entry.pack()
my_entry.focus()

#multiline
my_text = Text(width=30, height=5)
my_text.pack()

#scale
def scale_selected(value):
    print(value)
my_scale = Scale(from_=0, to=50, command=scale_selected)
my_scale.pack()

#spinbox
def spinbox_selected():
    print(my_spinbox.get())
my_spinbox = Spinbox(from_=0, to=100, command=spinbox_selected)
my_spinbox.pack()

#checkbutton
def check_selected():
    print(check_state.get())
check_state = IntVar()
my_check = Checkbutton(text="check", variable=check_state, command=check_selected)
my_check.pack()

#radiobutton
def radio_selected():
    print(radio_state.get())
radio_state = IntVar()
my_radiobutton1 = Radiobutton(text="Option 1", variable=radio_state, value=10, command=radio_selected)
my_radiobutton2 = Radiobutton(text="Option 2", variable=radio_state, value=20, command=radio_selected)
my_radiobutton1.pack()
my_radiobutton2.pack()

#listbox
def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox()
name_list = ["Furkan", "Ulaş", "Baki", "Mevlana"]
for i in range(len(name_list)):
    my_listbox.insert(i, name_list[i])
my_listbox.bind("<<ListboxSelect>>", listbox_selected)
my_listbox.pack()
window.mainloop()


