# Monster Quiz
CS467 Project - Team West Coast Monster App
  * Team Member: Zhaowei Si
  * Team Member: Ruosha Pang
  * Team Member: Gan Li

## Project prerequest-backend
```
sudo apt install python3.8
python3.8 -m pip install Django
python3.8 -m pip install djangorestframework
python3.8 -m pip install django-cors-headers
```

## How to run
1. at monster_quiz_backend directory, run `python3.8 manage.py runserver`
2. then cd to vue_monster_quiz directory to set up and run the frontend <br/>
With both backend and frontend running, the Monster Quiz is available at http://localhost:8080/

## dependencies
1. follow the link to install pip if you don't have one. https://pip.pypa.io/en/stable/installation/ <br/>
2. A few dependencies need to installed, follow this:
https://blog.logrocket.com/how-to-build-vue-js-app-django-rest-framework/#why-vuejs-django-rest-framework 


## How to create superuser for database
```python3.8 manage.py createsuperuser```
default username: admin
make up an email
remember to record your password