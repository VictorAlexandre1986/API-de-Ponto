from sqlalchemy import Column, Integer, String


def get_db():
    from app import db  # Importa db somente quando necessário
    return db

class LoginEnterprise(get_db().Model):
    __tablename__ = 'login_enterprise'

    id = get_db().Column(get_db().Integer, primary_key=True)
    username = get_db().Column(get_db().String(50), nullable=False, unique=True)
    password = get_db().Column(get_db().String(50), nullable=False, unique=True)
    email = get_db().Column(get_db().String(100), unique=True, nullable=False)
    # enterprise = get_db().relationship('Enterprise', uselist=False)    # Relacionamento com User (uselist=False garante relacionamento um-para-um)
  # Relacionamento com User (uselist=False garante relacionamento um-para-um)
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f'<Login {self.username}>'