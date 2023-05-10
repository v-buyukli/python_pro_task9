# python_pro_task9
____
**Get started**

1. Clone repository
2. Install requirements:

    `pip install -r requirements.txt`

3. Migrate command:

    `python manage.py migrate`

4. Run RabbitMQ on Docker:

    `docker run -d -p 5672:5672 rabbitmq` 

5. Runserver command:

    `TWILIO_ACCOUNT_SID={account_sid} TWILIO_AUTH_TOKEN={auth_token} python manage.py runserver`,

   where: {account_sid} is your TWILIO_ACCOUNT_SID, {auth_token} is your TWILIO_AUTH_TOKEN

6. Starting the worker process:

    `celery -A python_pro_task9 worker -l INFO` 
