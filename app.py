from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)

    def json(self):
        return {'id':self.id, 'username':self.username, 'email':self.email}

db.create_all()

#test endpoint
@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'test route'}),200)

#create a user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(username=data['username'],email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify({'message':'user_created'}),201)
    except Exception as e:
        return make_response(jsonify({'message':f'error creating user:{str(e)}'}),500)

#get all users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return make_response(jsonify({'users':[user.json() for user in users]}),200)
    except Exception as e:
        return make_response(jsonify({'message':f'error getting user:{str(e)}'}),500)

#get single user by id
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            return make_response(jsonify({'users': user.json()}),200)
        else:
            return make_response(jsonify({'message':'user not found'}),404)
    except Exception as e:
        return make_response(jsonify({'message':f'error getting user:{str(e)}'}),500)

#update user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.username = data['username']
            user.email = data['email']
            db.session.commit()
            return make_response(jsonify({'message':'user updated'}),200)
        else:
            return make_response(jsonify({'message':'user not found'}),404)
    except Exception as e:
        return make_response(jsonify({'message':f'error updating user:{str(e)}'}),500)

#delete user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({'message':'user deleted'}),200)
        else:
            return make_response(jsonify({'message':'user not found'}),404)
    except Exception as e:
        return make_response(jsonify({'message':f'error deleting user:{str(e)}'}),500)








