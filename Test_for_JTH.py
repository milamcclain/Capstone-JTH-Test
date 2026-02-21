# Test_for_JTH.py

# Import necessary modules
import tkinter as tk
from tkinter import ttk

# Create a main window
root = tk.Tk()
root.title("Just the Heart")

# Define styles for bronze color and hover effect
style = ttk.Style()
style.configure('Bronze.TLabel', foreground="#cd7f32")  # Bronze Color
style.configure('Bronze.TButton', background="#cd7f32", hovercolor="#a76d47")  # Bronze with Light Hover Effect

# Create a label with the title
title_label = ttk.Label(root, text="Just the Heart", style='Bronze.TLabel')
title_label.pack(pady=20)

# Create a header
header_label = ttk.Label(root, text="Service Inquiry Form", style='Bronze.TLabel')
header_label.pack(pady=10)

# Create a submit button
submit_button = ttk.Button(root, text="Submit", style='Bronze.TButton')
submit_button.pack(pady=20)

# Run the main loop
root.mainloop()