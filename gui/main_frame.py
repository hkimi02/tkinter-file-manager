import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import imageio
from core.file_manager import FileManager
from gui.styles import set_custom_styles

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

        # File listbox
        self.file_listbox = tk.Listbox(self, width=50, height=10)
        self.file_listbox.pack(pady=5)

        # Button to delete file
        self.btn_delete_file = ttk.Button(self, text="Supprimer le fichier", command=self.delete_file, style="TButton")
        self.btn_delete_file.pack(pady=5)

        # Button to rename file
        self.btn_rename_file = ttk.Button(self, text="Renommer le fichier", command=self.rename_file, style="TButton")
        self.btn_rename_file.pack(pady=5)

        # Initialize FileManager
        self.file_manager = FileManager()

    def load_icon(self, filename):
        icon_path = os.path.join("resources", "icons", filename)
        icon = imageio.imread(icon_path)
        return icon

    def list_files(self):
        self.file_listbox.delete(0, tk.END)
        files = self.file_manager.list_files()
        for file in files:
            self.file_listbox.insert(tk.END, file)

    def delete_file(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            file_name = self.file_listbox.get(selected_index)
            if messagebox.askokcancel("Confirmation", f"Êtes-vous sûr de vouloir supprimer '{file_name}' ?"):
                self.file_manager.delete_file(file_name)
                self.list_files()  # Refresh file list after deletion

    def rename_file(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            file_name = self.file_listbox.get(selected_index)
            new_name = messagebox.askstring("Renommer le fichier", f"Entrez le nouveau nom pour '{file_name}'")
            if new_name:
                self.file_manager.rename_file(file_name, new_name)
                self.list_files()  # Refresh file list after renaming
