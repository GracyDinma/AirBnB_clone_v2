#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    """Define relationship with Place (one-to-many)"""
    places = relationship("Place", cascade="all, delete",
                          back_populates="user")

    email = ''
    password = ''
    first_name = ''
    last_name = ''
