from utils.db import magodb

class challenge():
    id = magodb.Column(magodb.Integer, primary_key=True)
    editor = magodb.Column(magodb.String(50), nullable=False)
    deporte = magodb.Column(magodb.String(50), nullable=False)
    fecha = magodb.Column(magodb.String(50), nullable=False)
    descripcion = magodb.Column(magodb.String(300), nullable=False)
    imagen = magodb.Column(magodb.String(300), nullable=True)
    video = magodb.Column(magodb.String(300), nullable=True)


    def __init__(self, editor, deporte, fecha, descripcion, imagen, video) -> None:
        self.editor= editor
        self.deporte = deporte
        self.fecha = fecha
        self.descripcion = descripcion
        self.imagen = imagen
        self.video = video



    def __repr__(self):
        return f"Order({self.id}, '{self.editor}', '{self.deporte}', '{self.fecha}', '{self.descripcion}', '{self.imagen}', '{self.video}')"