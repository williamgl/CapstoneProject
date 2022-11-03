# Back end Prerequisites

## Install PIP
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

## Install virtual environment and activate
### install virtual environment
```
brew install virtualenv
```
or 
```
pip install virtualenv
```
### activate virtual environment
```
virtualenv environment_3_8_2
source environment_3_8_2/bin/activate
```

## Install Dependencies
```
pip install django
pip install django-rest-framework
pip install django-cors-headers
pip install djoser
pip install pillow    
pip install stripe
```

# Back end run
In `monster_quiz_backend` run
```
python manage.py runserver
```
