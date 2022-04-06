import tkinter as tk

window = tk.Tk()
window.minsize(width=500, height=300)
window.config(padx=25, pady=25)

MILES_TO_KM = 1.609344

def calculate():
    km_value.config(text = int(miles_entry.get()) * MILES_TO_KM)

miles_entry = tk.Entry()
miles_entry.grid(row=0, column=1, padx=5)

miles_label = tk.Label(text="Miles")
miles_label.grid(row=0, column=2, padx=5)

equal_label = tk.Label(text="is equal to")
equal_label.grid(row=1, column=0, padx=5)

km_value = tk.Label(text="0")
km_value.grid(row=1, column=1, padx=5)

km_label = tk.Label(text="Km")
km_label.grid(row=1, column=2, padx=5)

calculate_button = tk.Button(text="Calculate", command=calculate)
calculate_button.grid(row=2,column=1)



window.mainloop()
