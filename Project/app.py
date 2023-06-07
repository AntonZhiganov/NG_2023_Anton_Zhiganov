from flask import Flask, render_template, url_for, request, flash, redirect, get_flashed_messages
from cryptography.fernet import Fernet
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = '11nbbn3m22nodp!2kfmd32'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(50), nullable = False)
    
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
    decrypted_data = cipher_call.decrypt(encrypt_data)
    return decrypted_data
    
# Home page route
@app.route('/main')
@app.route('/')
@app.route('/home')

def index ():
    data = "Encrypted data"
    encrypted_data = encrypt_data(data)
    return render_template("index.html", encrypted_data = encrypted_data)
    
# Registration pagr route
@app.route('/registr', methods =['POST', 'GET'] )

def registration ():
    if request.method == 'POST':
        username = request.form['username']
        password1 = request.form['password1']
        password2 = request.form['password2']
        
        existingUser = User.query.filter_by(username = username).first()
        if existingUser:
            flash('This User already registered', 'error')
            return redirect(url_for("registration"))
        
        if password1 and password1 == password2 :
            encrypted_password = encrypt_data(password1)
            newUser = User(username = username, password = encrypted_password)
            db.session.add(newUser)
            db.session.commit()
            
            return 'You have successfully registered'
        else:
            return 'Password do not mutch!'
        
    data = "Encrypted data"
    encrypted_data = encrypt_data(data)
    return render_template("newUser.html", encrypted_data = encrypted_data)
                 
# Start server
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        generate_Key()
    app.run(debug = True)