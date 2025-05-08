import  tkinter as tk

root =tk.Tk()
root.title("Label Example With  Tkinter")
root.geometry("400x400")
label = tk.Label(root,text ="Label Example With TkInter",bg="blue",fg="white")
label.pack(pady=20)
root.mainloop()