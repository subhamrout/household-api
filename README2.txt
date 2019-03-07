Problem Statement:- The project is about developing a household api which stores information of all the assets in the house
and and relevant tasks can be performed on assets,like,Kitchen and corresponding task: cleaning the kitchen, 
mopping the floor etc.,and worker_id:"1ser3". The workers have a unique worker id , so the system should organize 
the assets' information, the worker details and list of all tasks available, and assign them accordingly to the 
worker with a deadline. Thus building an efficient household management system.



9> From create_table.py, 4 tables are created assets,tasks,workers,allocateTasks and users

	1>The users table will contain all the information ,like user_id,username and password
	This is used for registration and authentication purpose
	
	1>assets table consist of asset_id and asset, 
	while executing  "http://127.0.0.1:5000/add-asset" on postman provide {"asset_id": ,"asset":}
	as this is a POST method, and used to add asset 
	2>"http://127.0.0.1:5000/assets/all" will give all the asset that are stored in the database
	
	
	1> tasks table consist of task_id and tasks,
	while executing "http://127.0.0.1:5000/add-task" on postman provide {"task_id","tasks"}
	this is a POST method , and used to add task 
	
	
	1>workers table consist of worker_id and worker,
	while executing "http://127.0.0.1:5000/add-worker" on postman provide {"worker_id","worker_name"}
	this is a POST method , and used to add worker_id, and worker name

	
	1>allocateTasks table consist of an id , asset_id , task_id,worker_id, timeOfAllocation, Endtime
	Basically this table consist of which worker has to do which task on which asset and what is the 
	allocated time and what is the dead line
	2>execute "http://127.0.0.1:5000/get-task-for-worker/<string:worker_id>" ,which is a GET method 
	provide "worker_id" in the url and it will provide all the tasks and asset that is allocated to that 
	worker.
	3>execute "http://127.0.0.1:5000/allocate-task/" and provide {"asset_id":,"task_id":,"worker_id":,
									"timeOfAllocation":,"Endtime":}
		
10> To access heroku deployed app used "https://household-api-first.herokuapp.com/" instead of "http://127.0.0.1:5000/" and all the end points will remain same	