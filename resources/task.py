# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:32:53 2019

@author: Subham Rout
"""
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.task import TaskModel

class Task(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('task_id',type=str,required=True,
                        help= "this field cannot left blank")
    parser.add_argument('task',type=str,required=True,
                        help= "this field cannot left blank")
    @jwt_required()
    def post(self):
        data = Task.parser.parse_args()
        try:
            TaskModel.save_to_db(data)
        except:
            return {"Message":"An error occured while adding task to the db"}
        return {"Message": "Task sucessfully added"}
    