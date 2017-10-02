from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
# package created for password hashing
from passlib.apps import custom_app_context as pwd_context

Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    password_hash = Column(String(64))

    # takes password as argument and stores hash in the user table
    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    # this method will be called when a new user registers or changes their password on the system 
    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


engine = create_engine('sqlite:///users.db')
 

Base.metadata.create_all(engine)
    
