"""
Файл с моделями приложения.
"""

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db, login

class City(db.Model):
    """Тут хранятся записи городов с сопутствующими данными.
    Решил хранить все данные в одной табличке (я о континентах)
    т.к. данные однообразные.
    """

    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255))
    country = db.Column(db.String(255))
    continent = db.Column(db.String(255))
    population = db.Column(db.Integer)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(140), unique=True)
    password_hash = db.Column(db.String(255), default=None)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    """Показываем модулю flask-login как загружать текущего пользователя"""
    return User.query.get(int(id))
