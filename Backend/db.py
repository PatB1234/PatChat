import sqlite3 as driver
from sqlite3.dbapi2 import Cursor
from pydantic import BaseModel
from typing import Optional
import os
import jwt
from passlib.context import CryptContext
from datetime import date, datetime, timedelta
import random

DB = "chatapp.db"


class Users(BaseModel):

    username: str
    email: str
    password: str
    phoneNumber: Optional(int) = None
    uid: int


class ChatData(BaseModel):

    date: str
    name: str


class Message(BaseModel):

    message: str
    sentByID: int
    sentByName: str


SECRET_KEY = '67FEFF445D4DB9985DAB3CBD92BD7'
ALGORITHM = "HS256"
