import tkinter as tk

window = tk.Tk()
window.title("Hello from Pasha")

hello_world = tk.Label(
    text = "Hello World.",
    anchor = "nw",
    width = 32,
    height = 9,
    bd = 5,
)
hello_world.pack(padx = 5, pady = 5) #packs the widget to the window with padding


button = tk.Button(
    text = "Okay",
    font = (None, 24),
    bg = "grey64",
    fg = "blue",
    borderwidth = 1,
    relief = "raised",
    command=window.quit,
)
button.pack(padx = 10, pady = 10)

window.mainloop()
