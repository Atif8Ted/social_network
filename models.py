from peewee import *
import datetime
from flask.ext.login import UserMixin

DATABASE=SqliteDatabase('socila.db')
class User(Model):
    user_name=CharField(unique=True)
    email=CharField(unique=True)
    password=CharField(max_length=100)
    joined_at=DateTimeField(default=datetime.datetime.now)
    is_admin=BooleanField(default=False)

    class Meta:
        database=DATABASE
        order_by=('-joined_at',)

