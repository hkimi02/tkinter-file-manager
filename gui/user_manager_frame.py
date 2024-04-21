# user_manager_frame.py
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from core.user_manager import UserManager

class UserManagerFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.user_manager = UserManager()

        # Label for the user manager frame
        self.label = ttk.Label(self, text="User Manager")
        self.label.pack(pady=10)

        # Button to list users
        self.btn_list_users = ttk.Button(self, text="List Users", command=self.list_users)
        self.btn_list_users.pack(pady=5)

        # Button to add user
        self.btn_add_user = ttk.Button(self, text="Add User", command=self.add_user)
        self.btn_add_user.pack(pady=5)

        # Button to delete user
        self.btn_delete_user = ttk.Button(self, text="Delete User", command=self.delete_user)
        self.btn_delete_user.pack(pady=5)

        # Button to change password
        self.btn_change_password = ttk.Button(self, text="Change Password", command=self.change_password)
        self.btn_change_password.pack(pady=5)

    def list_users(self):
        users = self.user_manager.list_users()
        user_list = "\n".join(users)
        if user_list:
            tk.messagebox.showinfo("List of Users", user_list)
        else:
            tk.messagebox.showinfo("List of Users", "No users found.")

    def add_user(self):
        username = simpledialog.askstring("Add User", "Enter username:")
        if username:
            password = simpledialog.askstring("Add User", "Enter password:")
            if password:
                self.user_manager.add_user(username, password)
                tk.messagebox.showinfo("User Added", f"User '{username}' added successfully.")

    def delete_user(self):
        username = simpledialog.askstring("Delete User", "Enter username:")
        if username:
            self.user_manager.delete_user(username)
            tk.messagebox.showinfo("User Deleted", f"User '{username}' deleted successfully.")

    def change_password(self):
        username = simpledialog.askstring("Change Password", "Enter username:")
        if username:
            new_password = simpledialog.askstring("Change Password", "Enter new password:")
            if new_password:
                self.user_manager.change_password(username, new_password)
                tk.messagebox.showinfo("Password Changed", f"Password for user '{username}' changed successfully.")
