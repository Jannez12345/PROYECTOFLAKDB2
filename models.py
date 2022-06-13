#crear modelo persona
from app import db


class Persona(db.Model):
    id=db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(250), nullable=False)
    apellido = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)

    def __str__(self):
        return (
            f'Id: {self.id},'
            f'Nombre: {self.nombre},'
            f'Apellido :  {self.apellido},'
            f'Email : {self.email}'
        )


