from peewee import *
import datetime
from flask.ext.login import UserMixin #for login
from flask.ext.bcrypt import generate_password_hash #for bcrypt hash passwords

DATABASE=SqliteDatabase('socila.db')
class User(UserMixin,Model)
    username=CharField(unique=True)
    email=CharField(unique=True)
    password=CharField(max_length=100)
    joined_at=DateTimeField(default=datetime.datetime.now)
    is_admin=BooleanField(default=False)

    class Meta:
        database=DATABASE
        order_by=('-joined_at',)#sort by joining date

    @classmethod
    def create_user(cls,username,email,password,admin=False):
        try:
            cls.create(
                username=username,
                email=email,
                password=generate_password_hash(password),
                is_admin=admin
            )
        except IntegrityError:
            raise ValueError("User already exists")
