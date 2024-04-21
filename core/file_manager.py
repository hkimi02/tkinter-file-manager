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
        try:
            subprocess.run(['rm', filename])
            messagebox.showinfo("Fichier supprimé", f"Le fichier {filename} a été supprimé avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite lors de la suppression du fichier : {str(e)}")

    def rename_file(self, old_name, new_name):
        try:
            subprocess.run(['mv', old_name, new_name])
            messagebox.showinfo("Fichier renommé", f"Le fichier {old_name} a été renommé en {new_name}.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite lors du renommage du fichier : {str(e)}")
