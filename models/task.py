# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:38:48 2019

@author: Subham Rout
"""

import sqlite3

class TaskModel:
    
    def save_to_db(data):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO tasks VALUES (?,?)"
        cursor.execute(query,(data['task_id'],data['task']))
        connection.commit()
        connection.close()
        
    