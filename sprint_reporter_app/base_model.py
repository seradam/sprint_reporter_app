from peewee import *
import getpass

db = PostgresqlDatabase(str(getpass.getuser()), user=str(getpass.getuser()))



class BaseModel(Model):
    class Meta:
        database = db
