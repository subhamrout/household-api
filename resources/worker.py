# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:43:00 2019

@author: Subham Rout
"""

from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.worker import WorkerModel

class Worker(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('worker_id',type=str,required=True,
                        help= "this field cannot left blank")
    parser.add_argument('worker_name',type=str,required=True,
                        help= "this field cannot left blank")
    @jwt_required()
    def post(self):
        data = Worker.parser.parse_args()
        try:
            WorkerModel.save_to_db(data)
        except:
            return {"Message":"error occured while adding worker detail to db"}
        return {"Message":"Worker details sucessfully added "}
    
class WorkerTask(Resource):
    @jwt_required()
    def get(self,worker_id):
        try:
            return {"Tasks are:": WorkerModel. get_task_for_worker(worker_id)}
        except:
            return {"message":"Error occured while retriveving task for worker"}
            