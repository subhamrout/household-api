# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 22:01:39 2019

@author: Subham Rout
"""

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.allocatetask import AllocateTaskModel

class AllocateTask(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('asset_id',type=str,required=True,
                        help="This field cannot be left blank")
    parser.add_argument('task_id',type=str,required=True,
                        help="This field cannot be left blank")
    parser.add_argument('worker_id',type=str,required=True,
                        help="This field cannot be left blank")
    parser.add_argument('timeOfAllocation',type=str,required=True,
                        help="This field cannot be left blank")
    parser.add_argument('EndDate',type=str,required=True,
                        help="This field cannot be left blank")
    @jwt_required()
    def post(self):
        data = AllocateTask.parser.parse_args()
        try:
            AllocateTaskModel.save_to_db(data)
        except:
            return {"Message":"An error occured while adding data to allocatedTask table"}
        return {"Message":"Data sucessfully added."}