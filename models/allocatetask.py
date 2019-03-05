# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 22:12:39 2019

@author: Subham Rout
"""

import sqlite3


class AllocateTaskModel:
    
    def save_to_db(data):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO allocateTasks VALUES (NULL,?,?,?,?,?)"
        cursor.execute(query,(data['asset_id'],data['task_id'],
                                  data['worker_id'],data['timeOfAllocation'],
                                  data['EndDate']))
        connection.commit()
        connection.close()
        
        