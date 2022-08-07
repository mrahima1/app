from flask import Flask  # Import Flask class
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy class


app = Flask(__name__)  # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:147root!@localhost/application' # Set the connection string to connect to the database using an environment variable
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # Create SQLALchemy object

meal_ingredient = db.Table('meal_ingredient',
db.Column('meal_id', db.Integer, db.ForeignKey('meal.id'),
db.Column('ingredient.id', db.Integer, db.ForeignKey('ingredient.id'))))


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    made_from = db.relationship('Ingredient', secondary=meal_ingredient, backref='uses')


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


db.create_all()