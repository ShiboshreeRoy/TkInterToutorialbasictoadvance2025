import  tkinter as tk

import tkinter.messagebox as messagebox

# Create the main window
root = tk.Tk()
root.title("Message Box Example With Tkinter")
root.geometry("400x400")

# Function to show a message box when the button is clicked
def message_box():
    messagebox.showinfo("Information", "This is an information message box!")
def Warning_box():
    messagebox.showwarning("Warning", "This is a warning message box!")
def error_box():
    messagebox.showerror("Error", "This is an error message box!")

def ask_question():
    response = messagebox.askquestion("Question", "Do you want to proceed?")
    if response == "yes":
        messagebox.showinfo("Response", "You clicked Yes!")
    else:
        messagebox.showinfo("Response", "You clicked No!")


button =tk.Button(root,text="Show Info",bg="blue",fg="white", command=message_box)
button.pack(pady=20)

button2 =tk.Button(root,text="Show Warning",bg="blue",fg="white", command=Warning_box)
button2.pack(pady=20)

button3 =tk.Button(root,text="Show Error",bg="blue",fg="white", command=error_box)
button3.pack(pady=20)
button4 =tk.Button(root,text="Ask Question",bg="blue",fg="white", command=ask_question)
button4.pack(pady=20)

# Run the application
root.mainloop()