from flask import Flask, render_template, url_for, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate and upload an encryption key
def generate_Key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file: # Create or open file in binary write mode
        key_file.write(key)

# Reading data
def load_key():
    return open('key.key', 'rb').read()

# Data encryption 
def encrypt_data(data):
    key = load_key()
    cipher_call = Fernet(key)
    encrypted_data = cipher_call.encrypt(data.encode())
    return encrypted_data

# Data decryption
def decrypt_data(encrypt_data):
    key = load_key()
    cipher_call = Fernet(key)
    decrypted_data = cipher_call.decrypt(encrypt_data.encode())
    return decrypted_data
    
# Home page route
@app.route('/main')
@app.route('/')
@app.route('/home')

def index ():
    data = "Encrypted data"
    encrypted_data = encrypt_data(data)
    return render_template("index.html", encrypted_data = encrypted_data)

# Start server
if __name__ == '__main__':
    generate_Key()
    app.run(debug = True)