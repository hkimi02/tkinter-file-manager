# core/user_manager.py
import subprocess

class UserManager:
    def __init__(self):
        pass

    def list_users(self):
        try:
            result = subprocess.run(['cat', '/etc/passwd'], capture_output=True, text=True)
            output = result.stdout
            users = [line.split(':')[0] for line in output.split('\n') if line.strip()]
            return users
        except Exception as e:
            print(f"Error listing users: {e}")
            return []

    def add_user(self, username, password):
        subprocess.run(['sudo', 'useradd', '-m', '-p', password, username])

    def delete_user(self, username):
        subprocess.run(['sudo', 'userdel', '-r', username])

    def change_password(self, username, new_password):
        subprocess.run(['sudo', 'usermod', '-p', new_password, username])
