# To_Do_App
## A Basic To-Do Web Application using Django Framework
### Features
- User Authentication - Users can register, login and logout
- Edit Tasks
- Completed Tasks are also saved - If a user wants to visit them later
- Created API End points to get the ```User Data``` and ```Tasks of a User```.

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
- API End Points
    > To get the User information - ```http://localhost:8000/profile_info/user=<Username>/```
    > To get the Tasks of a User - ```http://localhost:8000/user_tasks/user=<Username>/```

### Below is the screenshot of the Application
<img src="https://raw.githubusercontent.com/Ram-95/to_do_app/master/Tasks.JPG" width="960" height="690">
