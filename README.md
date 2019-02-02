# messenger_app


Using the application

    Sign Up to create an account
    Login with the created account (you are now online)
    for first time you will not see users list as you are the only user in the system
    Open another browser (if you are using chrome, just open new incognito tab) and go to http://127.0.0.1:8000
    Repeat 1, 2 & 3 as many as you want more accounts to be online
    You can send messages to any user in the system either he/she is online or offline

Attachments

    Screenshots for the application

To Run the application

    create virtualenv and then activate the virtualenv
    install all the dependencies given in the requirement.txt by command pip install -r requirements.txt
    start the project by command django-admin startproject Messenger . 
    Make the app by the command django-admin startapp chat_app
    For the database, I have used MySQL-DB.
    Then, migrate the models used in this application by command python manage.py makemigrations and then by the command python manage.py migrate
    For running the server, do python manage.py runserver to check the application running.
