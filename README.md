# dd-Api

## General Project Status
 
 Currently the project is a **WIP** and is being developed by a team of students at **Cal Poly, San Luis Obispo**. The goal of the project is to have a working **API** system for [digitaldemocracy.org](http://digitaldemocracy.org/), for others to use to get information about various legislative hearings.


## Running the API


### To Run Locally

1. In the `settings.py` file, change where the database is located. The `host` field should be `api.digitaldemocracy.org`. The `settings.py` file **databases** field should look like below

	![Database config in settings_py](Database config in settings_py.png)
	
2. On the server log into the **MySQL** database
	
	```
	mysql -u admin -p
	```
	Enter the password as well after the above command

3. 	Grant all priviledges to your **IP address** in the **mysql** shell

	```
	GRANT ALL PRIVILEGES ON DDAPIwebsiteDB.* TO admin@'<your public ip>' IDENTIFIED BY '<password>';
	```
	```
	FLUSH PRIVILEGES;
	```

Now you can run from your local IDE

### To Run Remotely
To run the remotely server live at [api.digitaldemocracy.org](http://api.digitaldemocracy.org/) on the **Amazon EC2 instance** follow these instructions


1. In the `settings.py` file, change where the database is located. The `host` field should be `127.0.0.1`. The db is on the same instances so we enter `localhost` for the `HOST` location. The `settings.py` file **databases** field should look like below

	![Database remote config in settings_py](Database remot config in settings_py.png)
	
2. In the directory DDAPIwebsite on the server run the server on port `80`
	
	```
	sudo python3 manage.py runserver 0.0.0.0:80
	```

Now the app should run remotely from the server and can be accessed
from [api.digitaldemocracy.org](http://api.digitaldemocracy.org/)


### Python Config

This project is using **Python3** so we use `pip3` for installing. 

If you need to install mysql locally make sure to down these one has to work

 ```
 pip3 install PyMySQL
 ```
 
 ```
 pip3 install mysqlclient
 ``` 
 
 For **Macs** use **homebrew** to install `mysql`
 
 ```
 brew install mysql
 ```
  
 ```
 LDFLAGS=-L/usr/local/opt/openssl/lib pip install mysqlclient
 ```

