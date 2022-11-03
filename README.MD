# Monster Quiz
CS467 Project - Team West Coast Monster App
  * Team Member: Zhaowei Si
  * Team Member: Ruosha Pang
  * Team Member: Gan Li

## Instructions to run project locally
1.Clone the repository to your local.
2.Install all dependencies for the front end in [CapstoneProject/vue_monster_quiz/README.md](./vue_monster_quiz/README.md) and back end in [CapstoneProject/monster_quiz_backend/README.md](./monster_quiz_backend/README.md).
3. For back end, cd to the `monster_quiz_backend` directory, run ```python manage.py runserver```
4. For front end, cd to the `vue_monster_quiz` directory, run ```npm run serve```
With both backend and frontend running, the monster quiz app is available at http://localhost:8080/.

## Instructions to access database
1. After run ```python manage.py runserver``` in the `monster_quiz_backend` directory
2. The database server address is available at: http://127.0.0.1:8000/admin
3. Using credentials below to login to the database.
```username: admin 
password: database1
```


## How to create superuser for database
```python3.8 manage.py createsuperuser```
default username: admin
make up an email
remember to record your password
