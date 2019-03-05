# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 20:53:20 2019

@author: Subham Rout
"""

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from resources.user import UserRegister
from resources.asset import Asset,Asset_List
from resources.task import Task
from resources.worker import Worker , WorkerTask
from resources.allocatetask import AllocateTask


app = Flask(__name__)
app.secret_key = "SuBhAm$RoUt"
api = Api(app)

jwt = JWT(app,authenticate,identity)

api.add_resource(UserRegister,'/Register')
api.add_resource(Asset,'/add-asset')
api.add_resource(Asset_List,'/assets/all')
api.add_resource(Task,'/add-task')
api.add_resource(Worker,'/add-worker')
api.add_resource(WorkerTask,"/get-task-for-worker/<string:worker_id>")
api.add_resource(AllocateTask,'/allocate-task/')



if __name__ == "__main__":
    app.run(port=5000,debug = True)