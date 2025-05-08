import tkinter as tk


# Create the main window
root =tk.Tk()
root.title("Button Example With Tkinter")
root.geometry("400x400")
# Create a button

buton = tk.Button(root,text="ClickMe!",bg="blue",fg="white")
buton.pack(pady=20)

root.mainloop()