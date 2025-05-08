import tkinter as tk


root = tk.Tk()
root.title("Entry Example With Tkinter")
root.geometry("300x200")


# Create an Entry
name = tk.StringVar() # Variable to store the name entered by the user
label = tk.Label(root,text  = "Enter Your Name:", bg="blue",fg="white")
label.pack(pady=20)
entry =tk.Entry(root,textvariable=name)
entry.pack(pady=20)
root.mainloop()