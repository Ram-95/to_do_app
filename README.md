# To_Do_App [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
## A Basic To-Do Web Application using Django Framework
### Features
- User Authentication - Users can register, login and logout
- Add, Edit, Mark tasks as Complete/Incomplete and Delete Tasks
- Created API End points to get the ```User Data``` and ```User Tasks```

### Steps to be followed for first time use
- Create an Environment variable `DJANGO_ENV=DEV` to run the app in local.
- Generate a secret key using the below code and save it to an Environment variable `SECRET_KEY`.
  ```python
  import secrets
  secret_key = secrets.token_hex()
  ```
- Install all the dependencies using the below command
  ```
  pip install -r requirements.txt
  ```
- Run the below command - This will create the tables (by the Model definition) in the Database
  ```
  python manage.py migrate
  ```
- Create an ```admin``` user by running these following command
  ```
  $ python manage.py createsuperuser
  ```
### API End Points

  - To get the User information - ```/api/profile_info/user=<Username>/```
  
  - To get the Tasks of a User - ```/api/user_tasks/user=<Username>/```
