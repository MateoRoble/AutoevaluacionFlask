from app.models.models import Usuario

from app import app, db
from flask import (
    jsonify,
    request
)

from app.schemas.schema import (
    UsuarioSchema
)

from flask.views import MethodView

class UsuarioAPI(MethodView):
    def get(self, User_id=None):
        if User_id is None:
            usuarios = Usuario.query.all()
            resultado = UsuarioSchema().dump(usuarios, many=True)
            return jsonify(resultado)

        else:
            usuario = Usuario.query.get(User_id)
            resultado = UsuarioSchema().dump(usuario)
            return jsonify(resultado)
    
    def post(self):
        user_json = UsuarioSchema().load(request.json)
        nombre = user_json.get('nombre')
        mail = user_json.get('mail')
        psw = user_json.get('psw')
        nuevo_usuario = Usuario(nombre=nombre, mail=mail, psw=psw)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return jsonify(UsuarioSchema().dump(nuevo_usuario))
    
app.add_url_rule('/user', view_func=UsuarioAPI.as_view('usuario'))
app.add_url_rule('/user/<User_id>', view_func=UsuarioAPI.as_view('usuario_por_id'))
