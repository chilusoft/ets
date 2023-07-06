FROM faucet/python3:latest

# use pipenv to install dependencies

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

RUN python manage.py makemigrations

RUN python manage.py migrate

# run the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000

