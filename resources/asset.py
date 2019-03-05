# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:18:42 2019

@author: Subham Rout
"""

from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.asset import AssetModel


class Asset(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('asset_id',type=str,required=True,
                         help ="This field cannot be left blank")
    parser.add_argument('asset',type=str,required=True,
                         help ="This field cannot be left blank")
    
    @jwt_required()   
    def post(self):
        data = Asset.parser.parse_args()
        try:
            AssetModel.save_to_db(data)
        except:
            return {"Message":"Error occured while adding asset to the db"}
        return {"Message": "Asset addition to the db sucessful"}
    
        
class Asset_List(Resource):
    @jwt_required()
    def get(self):
        try:
            return {"The asset are : ": AssetModel.find_all()}
        except:
            return {"Message":"Erroe occured while returning all asset"}
        
        
        
        