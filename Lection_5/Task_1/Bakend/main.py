from flask import Flask, render_template, request

app = Flask(__name__)
users = {}
@app.route("/register", methods = ['GET', 'POST']) 
  
def register ():
    if request.method == 'GET' :
        username = str(request.args.get ('username'))
        password1 = str(request.args.get ('password1'))
        password2 = str(request.args.get ('password2'))
        
        if  password1 == password2 :
            users[username] = password1
            return 'Registration successful'
        else:
             return 'Passwords do not match'
         
    return ('/SingIn.HTML')

if __name__ == '__main__' :
    app.run(host = '0.0.0.0', port = 5000)