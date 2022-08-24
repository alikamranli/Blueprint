from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
main=Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
main.config['SECRET_KEY']="secretkey"
UPLOAD_FOLDER = './static/uploads/'
main.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

db=SQLAlchemy(main)
migrate=Migrate(main,db)
from models import *
from app.routes import *
from admin.routes import *



# import blueprints

from app import app_bp
from admin import admin_bp

# register blueprints

main.register_blueprint(app_bp)
main.register_blueprint(admin_bp)
db.create_all()
@main.route('/')
def index():
    return render_template('index.html')
if __name__=='__main__':
    main.run(debug=True)