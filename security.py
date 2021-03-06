# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:17:48 2019

@author: Subham Rout
"""


from  werkzeug.security import safe_str_cmp
import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel


def authenticate(username,password):
    user = UserModel.find_by_username(username=username)
    if user != None and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
    