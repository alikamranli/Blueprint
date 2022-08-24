from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SECRET_KEY']="secretkey"


db=SQLAlchemy(app)
migrate=Migrate(app,db)
from models import *
from app.routes import *
from admin.routes import *



# import blueprints

from app import app_bp
from admin import admin_bp

# register blueprints

app.register_blueprint(app_bp)
app.register_blueprint(admin_bp)
db.create_all()
@app.route('/')
def index():
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)