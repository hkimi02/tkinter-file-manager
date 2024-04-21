import tkinter as tk
from tkinter import ttk

def set_custom_styles():
    # Create a style object
    style = ttk.Style()

    # Set custom styles for buttons
    style.configure("TButton",
                    foreground="white",
                    background="#007bff",  # Ubuntu blue
                    padding=(10, 5),
                    font=("Helvetica", 10),
                    borderwidth=0)

    style.map("TButton",
                foreground=[('active', 'white')],
                background=[('active', '#0056b3')])  # Darker blue on hover

    # Set custom style for labels
    style.configure("TLabel",
                    background="#f0f0f0",  # Light gray background
                    font=("Helvetica", 12))

    # Set custom style for entry widgets
    style.configure("TEntry",
                    background="white",
                    foreground="black",
                    bordercolor="#007bff",  # Ubuntu blue
                    fieldbackground="white",
                    font=("Helvetica", 10),
                    relief=tk.SOLID,
                    padding=(5, 5))
