from app import db
from sqlalchemy import ForeignKey

class Usuario (db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100),unique=True, nullable=False)
    mail = db.Column(db.String(100), nullable=False)
    psw = db.Column(db.String(100), nullable=False)
    
class Categoria (db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    nombre_cat = db.Column(db.String(100), nullable=False)
    def __str__(self):
        return self.name

class Post (db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    autor = db.Column(db.String(100),nullable=False)
    contenido = db.Column(db.String(280),  nullable=False)
    titulo = db.Column(db.String(100),  nullable=False)
    fecha_creacion = db.Column(db.DateTime,  nullable=False)
    etiqueta_id = db.Column(db.Integer, ForeignKey('categoria.id'), nullable=False)
    etiqueta = db.relationship('Categoria', backref=db.backref('publicaciones', lazy=True))
    usuario_id = db.Column(db.Integer,db.ForeignKey('usuario.id'))
    usuario = db.relationship('Usuario',backref=db.backref('publicaciones', lazy=True))
    def __str__(self):
        return self.name

class Comentario (db.Model):
    __tablename__ = 'comentario'
    id = db.Column(db.Integer, primary_key=True)
    autor = db.Column(db.String(100),nullable=False)
    contenido = db.Column(db.String(140),  nullable=False)
    fecha_creacion = db.Column(db.DateTime,  nullable=False)
    id_post = db.Column(db.Integer, ForeignKey('post.id'), nullable=False)
    post = db.relationship('Post',backref=db.backref('comentarios', lazy=True))
    usuario_id = db.Column(db.Integer, ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario',backref=db.backref('comentarios', lazy=True))
    def __str__(self):
        return self.name
