import tkinter

#window
window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(width=500, height=300)

def click_button():
    user_input = my_entry.get()
    print(user_input)

#label (we use the label widget to display text)
my_label = tkinter.Label(text="This is my label", font=("Arial", 11, "bold"))
#my_label.config(bg="black", fg="white")
#my_label.pack(side="top")
my_label.grid(row=0, column=0)



#button
my_button = tkinter.Button(text="Click Me!", command=click_button)
#my_button.pack(side="top")
#my_button.place(x=250-30, y=150-16)
#my_button.update()
#print(my_button.winfo_width())
#print(my_button.winfo_height())
my_button.grid(row=1, column=1)

#entry (we use the entry widget to allow users to type text)
my_entry = tkinter.Entry(width=30)
#my_entry.pack(side="top")
my_entry.grid(row=3, column=2)



window.mainloop()
