"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Personaje, Weapon, Favorito, Place
from api.utils import generate_sitemap, APIException
# from admin import setup_admin
from flask_cors import CORS
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity 

api = Blueprint('api', __name__)
CURRENT_USER_ID=1

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/signup', methods=['POST'])
def signup():
    name = request.json.get("name", None)
    email =  request.json.get("email", None)
    password =  request.json.get("password", None)
    is_active =  request.json.get("is_active", True)
    
    if User.query.filter_by(email=email).first() is not None:
        return jsonify({"msg" : "user already exists"})
    
    new_user = User(name=name, email=email, password=password, is_active=is_active)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg" : "signup succesfully"})

@api.route('/login', methods=['POST'])
def login ():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    check_user = User.query.filter_by(email=email).first()

    if check_user is None:
        return jsonify({"msg" : "user doesnt exist"})
    
    elif password != check_user.password:
        return jsonify({"msg" : "password incorrect"})
    
    access_token = create_access_token(identity=check_user.email)
    return jsonify({"token": access_token, "user_id": check_user.id})

@api.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    result = [user.serialize() for user in users]
    return jsonify({"result" : result})


@api.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    try:
        current_user_email = get_jwt_identity()
        print(current_user_email)
        user = User.query.filter_by(email = current_user_email).first()
        print(user)

        if not user:
            return jsonify({"error": "User not found"}), 404

        return jsonify({
            "id": user.id,
            "email": user.email,
            "is_active": user.is_active
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@api.route('/addperson', methods=["POST"])
def add_person():
    name = request.json.get("name", None)
    race = request.json.get("race", None)
    height = request.json.get("height", None)

    new_person = Personaje(name=name, race=race, height=height)
    db.session.add(new_person)
    db.session.commit()
    return jsonify({"msg" : "person added succesfully"})

@api.route('/addweapon', methods=["POST"])
def add_weapon():
    name = request.json.get("name", None)
    type = request.json.get("type", None)
    built = request.json.get("built", None)

    new_weapon = Weapon(name=name, type=type, built=built)
    db.session.add(new_weapon)
    db.session.commit()
    return jsonify({"msg" : "weapon added succesfully"})

@api.route('/addplace', methods=["POST"])
def add_place():
    name = request.json.get("name", None)
    location = request.json.get("location", None)
    population = request.json.get("population", None)

    new_place = Place(name=name, location=location, population=population)
    db.session.add(new_place)
    db.session.commit()
    return jsonify({"msg" : "place added succesfully"})

@api.route('/favorite/person/<int:personaje_id>', methods=['POST'])
def add_favorite_person(personaje_id):
    existe = Favorito.query.filter_by(user_id=CURRENT_USER_ID, personaje_id=personaje_id).first()
    if existe is None:
        new_favorite = Favorito(user_id=CURRENT_USER_ID, personaje_id=personaje_id)
        db.session.add(new_favorite)
        db.session.commit()

        return jsonify({"msg" : "person added to favorites"})
    
@api.route('/favorite/weapon/<int:weapon_id>', methods=['POST'])
def add_favorite_weapon(weapon_id):
    existe = Favorito.query.filter_by(user_id=CURRENT_USER_ID, weapon_id=weapon_id).first()
    if existe is None:
        new_favorite = Favorito(user_id=CURRENT_USER_ID, weapon_id=weapon_id)
        db.session.add(new_favorite)
        db.session.commit()

        return jsonify({"msg" : "weapon added to favorites"})
    
@api.route('/favorite/place/<int:place_id>', methods=['POST'])
def add_favorite_place(place_id):
    existe = Favorito.query.filter_by(user_id=CURRENT_USER_ID, place_id=place_id).first()
    if existe is None:
        new_favorite = Favorito(user_id=CURRENT_USER_ID, place_id=place_id)
        db.session.add(new_favorite)
        db.session.commit()

        return jsonify({"msg" : "place added to favorites"})



    
    

    
       
    



