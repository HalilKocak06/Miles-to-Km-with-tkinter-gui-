import tkinter as tk

def miles_to_km():
    try:
        miles = float(miles_input.get())
        km = round(miles * 1.609)
        kilometer_result_label.config(text=f"{km}")
    except ValueError:
        kilometer_result_label.config(text="Invalid input")

window = tk.Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = tk.Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = tk.Label(text="0")
kilometer_result_label.grid(column=1, row=1)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = tk.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
