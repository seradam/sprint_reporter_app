from base_model import *

#ilyen szerkezetű táblát épít

class Sprint(BaseModel):
    sprint_id = PrimaryKeyField()
    title = CharField()
    user_story = TextField()
    acceptance_criteria = TextField()
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()
