# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:05:58 2019

@author: Subham Rout
"""

import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table1 = "CREATE TABLE IF NOT EXISTS assets (asset_id text PRIMARY KEY, assest text)"

create_table2 = "CREATE TABLE IF NOT EXISTS tasks (task_id text PRIMARY KEY ,task text)"

create_table3 = "CREATE TABLE IF NOT EXISTS workers (worker_id text PRIMARY KEY, name text)"

create_table4 = "CREATE TABLE IF NOT EXISTS allocateTasks (id text PRIMARY KEY,asset_id text,task_id text ,worker_id text, timeOfAllocation text,EndDate text)"

create_table5 = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text,password text)"

cursor.execute(create_table1)
cursor.execute(create_table2)
cursor.execute(create_table3)
cursor.execute(create_table4)
cursor.execute(create_table5)

connection.commit()
connection.close()



