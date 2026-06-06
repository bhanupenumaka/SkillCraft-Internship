import tkinter as tk

def convert():
    try:
        val = float(entry.get())
        unit = var.get()
        if unit == "Celsius to Fahrenheit":
            res = (val * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            res = (val - 32) * 5/9
        else:
            res = val + 273.15 # Celsius to Kelvin
        label_result.config(text=f"Result: {res:.2f}")
    except ValueError:
        label_result.config(text="Please enter a valid number")

root = tk.Tk()
root.title("Temperature Converter")

entry = tk.Entry(root)
entry.pack()

var = tk.StringVar(value="Celsius to Fahrenheit")
options = ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin"]
dropdown = tk.OptionMenu(root, var, *options)
dropdown.pack()

btn = tk.Button(root, text="Convert", command=convert)
btn.pack()

label_result = tk.Label(root, text="Result: ")
label_result.pack()

root.mainloop()
