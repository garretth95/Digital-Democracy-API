# dd-Api
api dev project
Read me for Digital Democracy API
WIP


TO RUN FROM SERVER AND PORT TO LOCAL MACHINE:

local machine:
$ ssh -i .ssh/ddkey -L 8080:localhost:80 <CP username>@api.digitaldemocracy.org

linux server:
[<CP username@ip}$ sudo python3 manage.py runserver 0.0.0.0:80