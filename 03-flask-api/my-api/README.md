# Usage

To execute "my-api" :
```
pip install flask --user
flask --app my-api --debug run -p 3000
```

Or, with Pipenv :
```
pipenv install flask
pipenv run flask --app my-api --debug run -p 3000
```

Or, with Docker :
```
docker init
docker compose up --build
```


Official Documentation - Quickstart :
https://flask.palletsprojects.com/en/3.0.x/quickstart/
