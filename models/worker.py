# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:49:11 2019

@author: Subham Rout
"""

import sqlite3

class WorkerModel:
    
    def save_to_db(data):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO workers VALUES (?,?)"
        cursor.execute(query,(data['worker_id'],data['worker_name']))
        connection.commit()
        connection.close()
    
    def get_task_for_worker(worker_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT task  FROM tasks WHERE task_id IN (SELECT task_id FROM allocateTasks WHERE worker_id = ?)"
        t_a_s_k =[]
        for row in cursor.execute(query,(worker_id,)):
            t_a_s_k.append(row)
        return t_a_s_k
    
        
        
        
        