import subprocess
from tkinter import messagebox

class FileManager:
    def list_files(self):
        result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        messagebox.showinfo("Liste des fichiers", output)

    def create_file(self, filename):
        if filename.strip() != "":
            subprocess.run(['touch', filename])
            messagebox.showinfo("Fichier créé", f"Le fichier {filename} a été créé avec succès.")
        else:
            messagebox.showwarning("Nom de fichier invalide", "Veuillez saisir un nom de fichier valide.")
    
    def delete_file(self, filename):
        if filename.strip() != "":
            subprocess.run(['rm','-r', filename])
            messagebox.showinfo("Fichier créé", f"Le fichier {filename} a été supprimé avec succès.")
        else:
            messagebox.showwarning("Nom de fichier invalide", "Veuillez saisir un nom de fichier valide.")
