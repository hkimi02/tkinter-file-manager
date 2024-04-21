# core/user_manager.py
import subprocess

class UserManager:
    def __init__(self):
        pass

    def list_users(self):
        result = subprocess.run(['cut', '-d:', '-f1', '/etc/passwd'], capture_output=True, text=True)
        users = result.stdout.split('\n')[:-1]  # Remove empty string from the end
        return users

    def add_user(self, username, password):
        subprocess.run(['sudo', 'useradd', '-m', '-p', password, username])

    def delete_user(self, username):
        subprocess.run(['sudo', 'userdel', '-r', username])

    def change_password(self, username, new_password):
        subprocess.run(['sudo', 'usermod', '-p', new_password, username])
