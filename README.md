# dd-Api
api dev project
Read me for Digital Democracy API
WIP

To run locally and connect to DB remotely:

make sure DATABASE settings are set host to remote

log into mysql with admin on remote server:
$ mysql -u admin -p

> GRANT ALL PRIVILEGES ON somedatabase.* TO someuser@'somehostname' IDENTIFIED BY 'password';
> FLUSH PRIVILEGES;

'somehostname' being your public IP and 'someuser' being admin

now you can run from your local IDE


To run remotely and connect to DB locally:

just make sure DATABASE settings are set host to local

in the first DDAPIwebsite app directory:
$ sudo python3 manage.py runserver 0.0.0.0:80

now the app should run remotely from the server and can be accessed
from api.digitaldemocracy.org
