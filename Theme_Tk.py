import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

app = ttk.Window(themename="cyborg")
ttk.Label(app, text="Styled App", bootstyle="info").pack()
# This code creates a simple GUI application using the ttkbootstrap library. It creates a window with a label that has a specific theme and style.


def on_button_click():
    messagebox.showinfo("Button Clicked", "You clicked the button!", parent=app)



ttk.Button(app, text="Click Me", bootstyle="success", command=on_button_click).pack(pady=10)

app.mainloop()
