# VideoAnalysisTool

#Instructions to run on local

install required libraries from requirements.txt file:

`pip install -r requirements.txt`


Create a .env file
```
touch .env
```


Make a new folder for logs
```
mkdir logs
```


update database parameters in .env file


update BASE_URL in settings.py
```
ngrok http 8000
```
update ngrok https url without trailing slash in settings.py BASE_URL


run local server using following command:
```
python manage.py runserver
```

Configure Postgres database before running migrations. Populate initial data using following command:
```
python manage.py makemigrations 
python manage.py migrate
```

