from flask import Blueprint
from flask import request
from flask.globals import request
from sqlalchemy import exc
from project.api.models import User
from project import db

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users/ping', methods=["GET"])
def ping_pong():
    return {"status": "success", 'message':"pong"}

@users_blueprint.route('/users', methods=["POST"])
def add_user():
    post_data = request.get_json()
    response_object = {"status":"fail", "message":"Invalid payload"}
    if not post_data:
        return response_object, 400

    username = post_data.get("username")
    email = post_data.get("email")
    try:
        user = User.query.filter_by(email=email).first()
        if not user:
            db.session.add(User(username=username, email=email))
            db.session.commit()
            response_object = {"status":"success", "message":f"{email} was added!"}
            return response_object, 201
        else:
            response_object = {"status":"fail", "message": "Sorry that email already exists."}
        return response_object, 400
    except exc.IntegrityError as e:
        db.session.rollback()
        return response_object, 400

@users_blueprint.route('/users/<user_id>', methods=["GET"])
def get_single_user(user_id):

    user = User.query.filter_by(id=user_id).first()
    response_object = {
        "status":"success",
        "data":{
            "id":user.id
        }
    }