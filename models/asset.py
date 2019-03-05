# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:28:19 2019

@author: Subham Rout
"""
import sqlite3


class AssetModel:       
    def save_to_db(data):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO assets VALUES (?,?)"
        cursor.execute(query,(data['asset_id'],data['asset']))
        connection.commit()
        connection.close()
    
    
    @classmethod
    def find_all(cls):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM assets"
        res = []
        for row in cursor.execute(query):
            res.append( {'id':row[0],'asset':row[1]})
        connection.close()
        return res