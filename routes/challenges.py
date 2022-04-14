from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required
from forms.challenges import ChallengesCreateForm, ChallengesUpdateForm
from utils.db import magodb
from models.challenges import Challenges
from werkzeug.utils import secure_filename
import os


challenges= Blueprint("challenges", __name__, url_prefix="/challenges")

#homepage de challenges
@challenges.route("/")
def home():
    return render_template("challenges/home.html")

#crear challenges
@challenges.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = ChallengesCreateForm()
    from app import app
    if form.validate_on_submit():
        editor=current_user.editoruser
        deporte = form.deporte.data
        fecha = form.fecha.data
        descripcion = form.descripcion.data
        imagen=form.imagen.data
       
        nombreimagen=secure_filename(imagen.filename)
        nombreunicoimg=str(uuid.uuid1()) + "_" + nombreimagen
        #sav image
        imagen.save(os.path.join(app.config['UPLOAD_FOLDER'], nombreunicoimg))
        #nombre de imagen en db
        imagen = nombreunicoimg
        #video
        video = form.video.data
        nombrevideo=secure_filename(video.filename)
        nombreunicovid=str(uuid.uuid1()) + "_" + nombrevideo
        #sav video
        video.save(os.path.join(app.config['UPLOAD_FOLDER'], nombreunicovid))
        #nombre de video en db
        video=nombreunicovid
        newChallenge = Challenges(editor, deporte, fecha, descripcion, imagen, video)
        magodb.session.add(newChallenge)
        magodb.session.commit()
        return redirect(url_for("noticias.home"))
    return render_template("noticias/create.html", form=form)

#delete a challenge 
@challenges.route("/delete/<int:id>")
@login_required
def delete(id):
    challenge = Challenges.query.get(id)
    magodb.session.delete (challenge)
    magodb.session.commit()
    return redirect(url_for("challenges.home"))

#update a challenge
@challenges.route("/challenges/update/<int:id>", methods=["GET", "POST"])
@login_required
def update(id):
        currentNew = Challenges.query.get(id)
        form = ChallengesUpdateForm()
        if request.method == "POST":
            currentNew.descripcion = form.descripcion.data
            currentNew.imagen = form.imagen.data
            magodb.session.commit()
            return redirect(url_for("noticias.home"))
        return render_template("noticias/update.html", form=form, currentNew=currentNew)
