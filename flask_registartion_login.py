"""
root@debian11-vm-26-199:~# curl -X POST -H "Content-Type: application/json" -d '{"username":"ajay","password":"john"}' http://localhost:5000/register
{
  "message": "User registered Successfully"
}
root@debian11-vm-26-199:~# curl -X POST -H "Content-Type: application/json" -d '{"username":"ajay","password":"john"}' http://localhost:5000/register
{
  "message": "User already exists"
}
root@debian11-vm-26-199:~# curl -X POST -H "Content-Type: application/json" -d '{"username":"ajay123","password":"john123"}' http://localhost:5000/register
{
  "message": "User registered Successfully"
}
root@debian11-vm-26-199:~# curl -X POST -H "Content-Type: application/json" -d '{"username":"ajay123","password":"john123"}' http://localhost:5000/login
{
  "message": "Login Successful"
}

"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/login_data.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Define a user model
class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(20), unique=True, nullable=False)
   password = db.Column(db.String(100), nullable=False)

   def __init__(self, username, password):
       self.username = username
       self.password = bcrypt.generate_password_hash(password).decode('utf-8')

with app.app_context():
   db.create_all()
@app.route('/register', methods=['POST'])
def register():
   data = request.get_json()
   username = data['username']
   password = data['password']
   print("jsd")
   if not username or not password:
       return josnify({'message': 'username and password are required'}),400

   if User.query.filter_by(username=username).first():
       return jsonify({'message': 'User already exists'}), 400

   new_user = User(username, password)
   db.session.add(new_user)
   db.session.commit()

   return jsonify({'message': 'User registered Successfully'})


@app.route('/login', methods=['POST'])
def login():
   data = request.get_json()
   username = data['username']
   password = data['password']

   user = User.query.filter_by(username=username).first()
   if user and bcrypt.check_password_hash(user.password, password):
       return jsonify({'message': 'Login Successful'})
   else:
       return jsonify({'message': 'Invalid credential'}), 401

if __name__=='__main__':
   app.run(debug=True)
                       



