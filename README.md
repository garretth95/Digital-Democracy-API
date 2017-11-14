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

'somehostname' being your public IP and 'sumeuser' being admin



To run remotely and connect to DB locally:

just make sure DATABASE setting is set host to local