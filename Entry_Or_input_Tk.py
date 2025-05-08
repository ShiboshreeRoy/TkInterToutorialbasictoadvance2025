import tkinter as tk


root = tk.Tk()
root.title("Entry Example With Tkinter")
root.geometry("300x200")


def GreetUser():
  name = entry.get() # Get the name entered by the user
  greeting = "Hello, " + name # Create a greeting message
  label = tk.Label(root, text=greeting, bg="blue", fg="white") # Create a label to display the greeting message
  label.pack(pady=20) # Pack the label into the window

# Create an Entry
name = tk.StringVar() # Variable to store the name entered by the user
label = tk.Label(root,text  = "Enter Your Name:", bg="blue",fg="white")
label.pack(pady=20)
entry =tk.Entry(root,textvariable=name)
entry.pack(pady=20)

button = tk.Button(root,text="Greet Me!",bg="blue",fg="white", command=GreetUser)
button.pack(pady=20)

root.mainloop()