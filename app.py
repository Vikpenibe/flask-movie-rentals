from flask import Flask, render_template, request
import json, os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db" 
db = SQLAlchemy(app)



class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    budget = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(10), nullable=False)
    cast = db.Column(db.String(100), nullable=False)



@app.route("/")
def index():
    db = Movies.query.all()
    return render_template("index.html", movies=db)



@app.route("/new-movie", methods=['POST', 'GET'])
def new_movie():


    if request.method == 'GET':
        return render_template("new_movie.html")
    else:
        #fetch movie details from request
        m = Movies()
        m.title = request.form['title']
        m.budget = request.form['budget']
        m.cast = request.form['cast']
        m.year = request.form['year']

        db.session.add(m)
        db.session.commit()

        return render_template(
            "new_movie.html",
            success= f"Movie '{m.title}' was successfuly added."
            )    








































# @app.route("/")
# def index():
#     movies = {}

#     if os.path.exists("movies.jason"):
#         with open("movies.json") as movies_file:
#            movies = json.load(movies_file)
    
#     else:
#         # create a file
#         with open("movies json", "w") as f:
#             f.write("[]")

       

#         new_movie = [{
#             "title": "Prison-Break",
#             "year": "2019",
#             "budget": "USD 700M",
#             "cast" : "People"
#         }]
#         movies = new_movie

#     return render_template("index.html", movies=movies)

# @app.route("/new-movie",methods=['POST', 'GET'])
# def new_movie():
#     if request.method =='GET':
#         return render_template("new_movie.html")
#     else:
#         new_movie = {}
#         new_movie['title'] = request.form['title']
#         new_movie['year'] = request.form['year']
#         new_movie['budget'] = request.form['budget']
#         new_movie['cast'] = request.form['cast']

#         with open("movies.json", "w") as f:
#             # f.write(str(new_movie))
#             json.dump(new_movie, f)
            
#         return render_template(
#             "new_movie.html",
#             success = f"Movie '{new_movie['title']}' was successfull added."
#         )
#         return new_movie
    