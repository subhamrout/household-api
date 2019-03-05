# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 22:41:44 2019

@author: Subham Rout
"""

from flask_restful import Resource,reqparse
import sqlite3
from models.user import UserModel
    


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type = str, required = True,
                        help = "This field cannot left blank")
    
    parser.add_argument("password", type = str, required = True,
                        help = "This field cannot left blank")
    
    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data["username"]):
            return {"message":"The user already exist"}
        
        connection  = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "INSERT INTO users VALUES (NULL,?,?)"
        cursor.execute(query,(data["username"],data["password"]))
        
        connection.commit()
        connection.close()
        
        return {"message":"User registration completed sucessfully"}