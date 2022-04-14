from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DateField, MultipleFileField, FileField, TextAreaField
from wtforms.validators import InputRequired, Length

class ChallengesCreateForm(FlaskForm):
    deporte = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=20),
        ],
        render_kw={"placeholder": "deporte"},
    )
    
    fecha= DateField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "fecha"},
    )
    
    descripcion = TextAreaField(
        validators=[
            InputRequired(),
            Length(min=4, max=300),
        ],
        render_kw={"placeholder": "descripcion"},
    )
    
    imagen = FileField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "imagenes"},
    )

    video = FileField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "videos"},
    )
    
    submit = SubmitField ("crear")

class ChallengesUpdateForm(FlaskForm):
    descripcion = TextAreaField(
        validators=[
            InputRequired(),
            Length(min=4, max=300),
        ],
        render_kw={"placeholder": "descripcion"},
    )
    
    imagen = MultipleFileField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "imagenes"},
    )

    video = FileField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "videos"},
    )
    
    submit = SubmitField ("crear")
