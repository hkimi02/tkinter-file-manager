# user_manager_frame.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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
        messagebox.showinfo("List of Users", "\n".join(users))

    def add_user(self):
        username = messagebox.askstring("Add User", "Enter username:")
        password = messagebox.askstring("Add User", "Enter password:")
        if username and password:
            self.user_manager.add_user(username, password)
            messagebox.showinfo("User Added", f"User '{username}' added successfully.")

    def delete_user(self):
        username = messagebox.askstring("Delete User", "Enter username:")
        if username:
            self.user_manager.delete_user(username)
            messagebox.showinfo("User Deleted", f"User '{username}' deleted successfully.")

    def change_password(self):
        username = messagebox.askstring("Change Password", "Enter username:")
        if username:
            new_password = messagebox.askstring("Change Password", "Enter new password:")
            if new_password:
                self.user_manager.change_password(username, new_password)
                messagebox.showinfo("Password Changed", f"Password for user '{username}' changed successfully.")
