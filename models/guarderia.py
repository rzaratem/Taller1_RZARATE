from db import db
from sqlalchemy import text

#from database.db import db

class Guarderia(db.Model):
    _tablename_ = 'guarderias'
    idGuarderia = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    Nombre_Guarderia = db.Column(db.String(120), nullable=False)
    Direccion = db.Column(db.String(100), nullable=True)
    Telefono = db.Column(db.Integer, nullable=True)  

class Cuidador(db.Model):
    _tablename_ = 'cuidadores'
    idCuidador = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    Nombre = db.Column(db.String(120), nullable=False)
    Telefono = db.Column(db.String(100), nullable=True)
    #Id_guarderia = db.Column(db.Integer, db.ForeignKey('guarderias.idGuarderia'), nullable=True)  

class Perros(db.Model):
    _tablename_ = 'perros'
    idPerros = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    Nombre_Perro = db.Column(db.String(120), nullable=False)
    Raza_Perro = db.Column(db.String(120), nullable=False)
    Edad = db.Column(db.Integer, nullable=True)  
    Peso = db.Column(db.Float, nullable=False)
    #Id_guarderia = db.Column(db.Integer, db.ForeignKey('guarderias.idGuarderia'), nullable=True)  
    #Id_Cuidador = db.Column(db.Integer, db.ForeignKey('cuidadores.idCuidador'), nullable=True)  





class User(db.Model):
    _tablename_ = 'user3'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    fullname = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(200))
    about_me = db.Column(db.String(140))
    #last_seen = db.Column(db.DateTime, default=datetime.utcnow)
  


    def _repr_(self):
        return f"<Perros {self.idPerros}>"

    def to_dict(self):
        return {
            "idPerros": self.idPerros,
            "Nombre_Perro": self.Nombre_Perro,
            "Raza_Perro": self.Raza_Perro,
            "Edad": self.Edad,
            "Peso": self.Peso
        }
