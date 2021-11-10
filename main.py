from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

## CREATE DATABASE

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(120), nullable=False)
    img_url = db.Column(db.String(120), nullable=False)

db.create_all()

#Edit form
class EditForm(FlaskForm):

    rating = StringField('Your rating out of 10 eg 7.5', validators=[DataRequired()] )
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField(label="Done")




@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == "POST":
        movie_id = request.form['id']


    else:
        edit_form = EditForm()
        edit_form.validate_on_submit()
        return render_template("edit.html", form=edit_form)

if __name__ == '__main__':
    app.run(debug=True)
