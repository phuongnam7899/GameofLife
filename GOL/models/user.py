from mongoengine import Document,StringField,IntField

class User(Document):
    username = StringField()
    password = StringField()
    name = StringField()
    age = IntField()
    city = StringField()
    mail = StringField()
    st = IntField()
    knl = IntField()
    cre = IntField()
    per = IntField()
    soc = IntField()    
