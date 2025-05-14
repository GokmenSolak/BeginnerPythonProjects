
from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)

def check_button():
    weight = user_weight_input.get().strip()
    height = user_height_input.get().strip()

    if weight == "" or height == "":
        result_label.config(text="Please enter values")
        return
    try:
        weight = float(weight)
        height = float(height)
    except ValueError:
        result_label.config(text = "Please enter numeric values")
        return

    bmi = round(weight / (height /100) ** 2, 1)

    if bmi < 18.5:
        result_label.config(text= f"Your BMI: {bmi}. You are underweight")
        return
    elif 18.5 <= bmi <= 24.9:
        result_label.config(text= F"Your BMI: {bmi}. You have a normal weight")
        return
    elif 25 <= bmi <= 29.9:
        result_label.config(text=f"Your BMI: {bmi}. You are overweight")
        return
    elif 30 <= bmi <= 34.9:
        result_label.config(text= f"Your BMI: {bmi}. You are class I obesity")
        return
    elif 35 <= bmi <= 39.9:
        result_label.config(text=f"Your BMI: {bmi}. You are class II obesity")
        return
    elif bmi >= 40:
        result_label.config(text=f"Your BMI: {bmi}. You are class III obesity")
        return
    else:
        result_label.config(text="Something went wrong")

user_weight = Label(text="Enter Your Weight (kg)", font=("Arial", 9, "normal"))
user_weight.pack(side="top")
user_weight.config(padx=10, pady=10)

user_weight_input = Entry(width=15)
user_weight_input.pack()
user_weight_input.focus()

user_height = Label(text="Enter Your Height (cm)", font=("Arial", 9, "normal"))
user_height.pack(side="top")
user_height.config(padx=10, pady=10)

user_height_input = Entry(width=15)
user_height_input.pack()

result_label = Label(text="", font=("Arial", 9, "normal"))
result_label.pack(side="top")

my_button = Button(text="Calculate", command=check_button)
my_button.pack(side="top")

window.mainloop()