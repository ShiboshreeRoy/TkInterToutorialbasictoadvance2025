import tkinter as tk


# Create the main window
root =tk.Tk()
root.title("Button Example With Tkinter")
root.geometry("400x400")

# Create a label to display the button click message
def on_button_click():
    label_result =tk.Label(root,text="Button Clicked!")
    label_result.pack(pady=20)


# Create a button

buton = tk.Button(root,text="ClickMe!",bg="blue",fg="white", command=on_button_click)
buton.pack(pady=20)



root.mainloop()