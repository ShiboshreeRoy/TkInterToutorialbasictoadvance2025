import tkinter as tk
from tkinter import Canvas

# Create the main window
root = tk.Tk()
root.title("Canvas Drawing Example")
root.geometry("600x400")
Canvas = Canvas(root, width=600, height=400, bg="white")
Canvas.pack()


# Draw a rectangle
Canvas.create_rectangle(50, 50, 150, 150, fill="blue", outline="black")
# Draw a circle
Canvas.create_oval(200, 50, 300, 150, fill="red", outline="black")

# Draw a line
Canvas.create_line(50, 200, 300, 200, fill="green", width=5)
# Draw text
Canvas.create_text(400, 100, text="Hello, Tkinter!", font=("Arial", 24), fill="purple")
# Draw a polygon (triangle)
Canvas.create_polygon(400, 200, 350, 300, 450, 300, fill="yellow", outline="black")

# Draw an arc
Canvas.create_arc(50, 250, 150, 350, start=0, extent=180, fill="orange", outline="black")
# Draw a rectangle with rounded corners
Canvas.create_rectangle(200, 250, 300, 350, fill="pink", outline="black", width=2, stipple="gray50")
# Draw a text with shadow effect
Canvas.create_text(400, 300, text="Shadow Text", font=("Arial", 24), fill="black")

root.mainloop()