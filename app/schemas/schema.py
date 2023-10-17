from app import ma

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'mail','psw')

class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre_cat')

class PostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'autor','contenido','titulo','fecha_creacion','titulo','etiqueta_id','etiqueta','usuario_id','usuario')

class ComentarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'autor','contenido','fecha_creacion','id_post','post','usuario_id','usuario')