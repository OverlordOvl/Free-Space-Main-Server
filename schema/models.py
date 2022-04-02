import os
import sys
import datetime
from dotenv import load_dotenv
from peewee import BooleanField, PostgresqlDatabase

from peewee import (
    CharField,
    DateTimeField,
    PrimaryKeyField,
    Model,
    IPField,
    ForeignKeyField,
)


load_dotenv()

db_handle = PostgresqlDatabase(
    database=os.getenv("PGDATABASE"),
    user=os.getenv("PGUSER"),
    password=os.getenv("PGPASSWORD"),
    host=os.getenv("PGHOST"),
)


class DBModel(Model):
    class Meta:
        database = db_handle


class BaseModel(DBModel):
    id = PrimaryKeyField(null=False)


class CreatedTracked(DBModel):
    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())


class Expired(DBModel):
    created_at = DateTimeField(default=datetime.datetime.now(), required=True)
    expires_at = DateTimeField(required=True)


class Server(BaseModel):
    ip = IPField()
    key = CharField(max_length=44, unique=True)
    invite_code = CharField(max_length=255, unique=True)
