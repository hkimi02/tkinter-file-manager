import os
import tkinter as tk
from tkinter import ttk
from core.file_manager import FileManager
from gui.styles import set_custom_styles
import imageio

class MainFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.bg_color = "#f0f0f0"  # Light gray background
        self.btn_color = "#007bff"  # Ubuntu blue
        self.btn_hover_color = "#0056b3"  # Darker blue on hover

        # Apply custom styles
        set_custom_styles()

        # Load icons
        self.folder_icon = self.load_icon("folder.png")
        self.file_icon = self.load_icon("file.png")

        # Label of welcome
        self.welcome_label = ttk.Label(self, text="Bienvenue dans l'interface de gestion des fichiers Unix")
        self.welcome_label.pack(pady=10)

        # Button to list files
        self.btn_list_files = ttk.Button(self, text="Lister les fichiers", command=self.list_files, style="TButton")
        self.btn_list_files.pack(pady=5)

        # Entry for filename
        self.filename_entry = ttk.Entry(self, width=30, style="TEntry")
        self.filename_entry.pack(pady=5)

        # Button to create a file
        self.btn_create_file = ttk.Button(self, text="Créer un fichier", command=self.create_file, style="TButton")
        self.btn_create_file.pack(pady=5)

        # Initialize FileManager
        self.file_manager = FileManager()

    def load_icon(self, filename):
        icon_path = os.path.join("resources", "icons", filename)
        icon = imageio.imread(icon_path)
        return icon

    def list_files(self):
        self.file_manager.list_files()

    def create_file(self):
        filename = self.filename_entry.get()
        self.file_manager.create_file(filename)
