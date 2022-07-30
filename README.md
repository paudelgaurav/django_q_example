## Example django project demonstrating usecase of django_Q

### How to run ?


##### Pull the code from the server.

##### Create virtual Environment
```sh
python3 -m venv .venv
```

##### Activate virtual Environment
```sh
source .venv/bin/activate 
```

##### Install requirements
```sh
pip install poetry
poetry install
```
 
##### Migrate model to database
go inside project folder and make sure environment is activated
```sh
python manage.py migrate
```

##### Run redis with docker
```sh
docker run --name redis-server -d redis
```

##### Run django_q cluster
```sh
python manage.py qcluster
```

##### Run project
```sh
python manage.py runserver
```
