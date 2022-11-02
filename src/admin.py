import os
from flask_admin import Admin
from .db import db

### Importar los modelos #####
from src.models import User, Vehicles, Favorite_Vehicles, Planets, Favorite_Planets, Character, Favorite_Character, TokenBlockedList

from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Vehicles, db.session))
    admin.add_view(ModelView(Favorite_Vehicles, db.session))
    admin.add_view(ModelView(Planets, db.session))
    admin.add_view(ModelView(Favorite_Planets, db.session))
    admin.add_view(ModelView(Character, db.session))
    admin.add_view(ModelView(Favorite_Character, db.session))
    admin.add_view(ModelView(TokenBlockedList, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))