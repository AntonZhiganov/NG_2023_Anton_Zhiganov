from flask import Flask, render_template, url_for, request, flash, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import hashlib
from flask_socketio import SocketIO, leave_room, emit

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = '11nbbn3m22nodp!2kfmd32'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
socketio = SocketIO(app)

# Associating the LoginManager with our code
login_manager = LoginManager()
login_manager.init_app(app)

# Database creation (Password)
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(50), nullable = False)
    
    # Add is_active attribute
    is_active  = db.Column(db.Boolean, default = True)
    is_admin = db.Column(db.Boolean, default = False)
 
    def is_authenticated(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return(str(self.id))

    
# Create a callback function decorator
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
# Database creation (Message)
class Message (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(600), nullable = False)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'), nullable = False)
    
# Database creation (Chats)
class Chat(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    owner_id = db.Column(db.Integer, nullable = False)
    secret = db.Column(db.String(50))
    messages = db.relationship('Message', backref = 'chat', lazy = True)
    secret_entered = db.Column(db.Boolean, default=False)
    
# MD5 encryption
def encrypt_data(data):
    md5_hash = hashlib.md5(data.encode()).hexdigest()
    return md5_hash
    
# Home page route
@app.route('/main')
@app.route('/')
@app.route('/home')

def index ():
    data = "Encrypted data"
    encrypted_data = encrypt_data(data)
    return render_template("index.html", encrypted_data = encrypted_data)
    
# Registration page route
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
                 
# login page route
@app.route('/login', methods = ['POST', 'GET'])

def login ():
    if current_user.is_authenticated:
        return redirect(url_for('chats'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username = username).first()
        if user:
            decrypted_password = encrypt_data(password)
            if decrypted_password == user.password:
                flash ('You have successfully logged in', 'success')
                login_user(user)
                return redirect(url_for("chats"))
            else:
                flash('Incorrect password', 'error')
        else:
            flash('User does not exist', 'error')
            
    data = "Encrypted data"
    encrypted_data = encrypt_data(data)
    return render_template("login.html", encrypted_data = encrypted_data)
                     
# Chats Page
@app.route ('/chats')
@login_required
def chats ():
    chats = Chat.query.all()
    return render_template("chatsPage.html", chats = chats)

# Add chat 
@app.route ('/add.chat', methods = ['POST'])
@login_required
def add_chat ():
    if request.method == 'POST':
        chat_name = request.form['chat_name']
        secret = request.form['secret']
        owner_id = current_user.id
        if secret:
            new_chat = Chat(name = chat_name, owner_id = owner_id, secret = secret)
        else:
            new_chat = Chat(name = chat_name, owner_id = owner_id)
        db.session.add(new_chat)
        db.session.commit()
        flash('New chat added successfully', 'success')
        return redirect(url_for('chats'))
     
# Delete chat                
@app.route('/delete_chat/<int:chat_id>', methods=['GET', 'POST'])
@login_required
def delete_chat(chat_id):
    chat = Chat.query.get(chat_id)
    if chat.owner_id != current_user.id:
        flash('У вас нет прав на удаление этого чата', 'danger')
        return redirect(url_for('chats'))
    if chat.messages:
        for message in chat.messages:
            db.session.delete(message)
    db.session.delete(chat)
    db.session.commit()
    flash('Чат успешно удален', 'success')
    return redirect(url_for('chats'))
        
# Open chat
@app.route('/chat/<int:chat_id>', methods=['GET', 'POST'])
@login_required
def open_chat(chat_id):
    chat = Chat.query.get_or_404(chat_id)
    secret_entered = session.get(f'secret_entered_{chat_id}_{current_user.id}', False)
    if chat.secret and not secret_entered:
        return redirect(url_for('chat_secret', chat_id=chat.id))
    if request.method == 'POST':
        content = request.form.get('content')
        if content:
            if not secret_entered:
                content = hashlib.md5(content.encode()).hexdigest()
            message = Message(content=content, chat_id=chat_id)
            db.session.add(message)
            db.session.commit()
            socketio.emit('new_message', {'content': content}, room=chat_id)
        return redirect(url_for('open_chat', chat_id=chat.id))
    else:
        messages = Message.query.filter_by(chat_id=chat_id).all()
        if not secret_entered:
            for message in messages:
                message.content = hashlib.md5(message.content.encode()).hexdigest()
        return render_template('chat.html', chat=chat, messages=messages)
 
# User authorization in the chat
def login_user_chat(chat):
    session['current_user'] = str(current_user.id)
    active_users = session.get('active_users', [])
    if str(current_user.id) not in active_users:
        active_users.append(str(current_user.id))
    session['active_users'] = active_users
    session['authenticated_chat_id'] = str(chat.id)     

# Chat secret
@app.route('/chat/<int:chat_id>/secret', methods=['GET', 'POST'])
@login_required
def chat_secret(chat_id):
    chat = Chat.query.get_or_404(chat_id)
    if request.method == 'POST':
        secret = request.form.get('secret')
        if secret == chat.secret:
            session[f'secret_entered_{chat_id}_{current_user.id}'] = True
            return redirect(url_for('open_chat', chat_id=chat.id))
    return render_template('chat_secret.html', chat=chat)
    
# Leave user from chat
@socketio.on('leave')
def on_leave(data):
    chat_id = data['chat_id']
    leave_room(chat_id)
    emit('status', {'msg': 'You have left the chat'}, room=chat_id)

# logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
        
# Start server
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, port = 3030, debug = True)