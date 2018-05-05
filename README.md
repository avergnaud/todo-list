https://developers.google.com/calendar/quickstart/python

.gitignore

# install

apt-get install sqlite

pip install flask

pip install flask_sqlalchemy

pip install --upgrade google-api-python-client

# run

# troubleshooting

FileNotFoundError: [Errno 2] No such file or directory: 'client_secret.json'
> https://developers.google.com/calendar/quickstart/python

scp /home/ubuntu/dev3/seriahi/todo-list/client_secret.json pi@192.168.1.32:/home/pi/dev/todo-list/client_secret.json
scp /home/ubuntu/dev3/seriahi/todo-list/credentials.json pi@192.168.1.32:/home/pi/dev/todo-list/credentials.json