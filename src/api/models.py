from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorito = db.relationship("Favorito", backref="user", lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Personaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    race = db.Column(db.String(80))
    height = db.Column(db.Integer)
    favorito = db.relationship("Favorito", backref="personaje", lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "race": self.race,
            "height": self.height
            # do not serialize the password, its a security breach
        }

class Weapon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    type = db.Column(db.String(80))
    built = db.Column(db.String(80))
    favorito = db.relationship("Favorito", backref="weapon", lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "built": self.built
            }
    

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    location =  db.Column(db.String(80))
    population = db.Column(db.Integer)
    favorito = db.relationship("Favorito", backref="place", lazy=True)


class Favorito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    personaje_id = db.Column(db.Integer,db.ForeignKey("personaje.id"))
    weapon_id = db.Column(db.Integer,db.ForeignKey("weapon.id"))
    place_id = db.Column(db.Integer,db.ForeignKey("place.id"))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "personaje_id": self.personaje.serialize() if self.personaje else None,
            "weapon_id": self.weapon.serialize() if self.weapon else None,
            "place_id": self.place.serialize() if self.place else None,
            }
    

