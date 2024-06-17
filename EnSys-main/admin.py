import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def create_db():
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_admin(username, password):
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)
    cursor.execute('INSERT INTO admins (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    conn.close()

def get_admin(username):
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM admins WHERE username = ?', (username,))
    admin = cursor.fetchone()
    conn.close()
    return admin

def validate_admin(username, password):
    admin = get_admin(username)
    if admin and check_password_hash(admin[2], password):
        return True
    return False

if __name__ == '__main__':
    create_db()
    # Add a default admin user (replace 'admin' and 'password' with your desired credentials)
    add_admin('admin', 'password')
