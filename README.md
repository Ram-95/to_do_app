# To_Do_App [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
## A Basic To-Do Web Application using Django Framework
### Features
- User Authentication - Users can register, login and logout
- Add, Edit, Mark tasks as Complete/Incomplete and Delete Tasks
- Created API End points to get the ```User Data``` and ```User Tasks```

### Steps to be followed for first time use
- Run these commands - This will create your Tables (by the Model definition) in the Database
```
python manage.py migrate

python manage.py makemigrations

python manage.py migrate
```
- Create an ```admin``` user by running these following commands
```
$ python manage.py createsuperuser
```
### API End Points

  - To get the User information - ```/api/profile_info/user=<Username>/```
  
  - To get the Tasks of a User - ```/api/user_tasks/user=<Username>/```

### Below is the screenshot of the Application

<img src="https://raw.githubusercontent.com/Ram-95/to_do_app/master/Tasks.JPG">


#### See live at: https://to-do-app-pydj.herokuapp.com/
- Use the following as credentials to checkout the application.
  - Username: **TestUser**
  - Password: **Passuser@123**

- **PS**: *Do NOT upload any profile picture as I have not configured any Amazon S3 bucket.*
