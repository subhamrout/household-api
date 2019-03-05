1> TO know about the libraries used refer requirements.txt
2> First of all run create_table.py to create the data.db (database)
3> then execute the app.py 
4> The Api is tested on postman locally and also deployed on  heroku by using the github  (https://github.com/subhamrout/household-api.git)
5> there are two seperate file ,models and recources 
6> The models folder basically contains all the file that interact with the database
7> The resources folder is for user interaction auch as GET,POST etc
8> A security.py file is added for additional authentication ,for extra protection 

you can use http://127.0.0.1:5000/Register  on postman  to register username and password
and  http://127.0.0.1:5000/auth to get a autherization key for further use