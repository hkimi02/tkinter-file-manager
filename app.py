import tkinter as tk
from gui.main_frame import MainFrame

class UnixFileManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion des fichiers Unix")
        self.main_frame = MainFrame(self)
        self.main_frame.pack(padx=20, pady=20)

if __name__ == "__main__":
    app = UnixFileManagerApp()
    app.mainloop()