# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Server(peewee.Model):
    id = PrimaryKeyField(primary_key=True)
    ip = IPField()
    key = CharField(max_length=44, unique=True)
    invite_code = CharField(max_length=255, unique=True)


    class Meta:
        table_name = "server"
