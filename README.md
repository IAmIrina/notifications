# Project work: "Notification service for Online cinema.".

The service allows users to be notified about different events, such as confirmation of registration, new releases, analytics, etc.

The service implements e-mail notifications, but using interfaces in the source code allows for easy integration in other ways, such as SMS, Telegram messages, etc.

## Schema of the service
![image](https://user-images.githubusercontent.com/78168466/198252273-3ccf5c86-26de-4cc5-bb7c-7dde8c28127c.png)

## Schema Sender module
![image](https://user-images.githubusercontent.com/78168466/198835048-96d53d8c-2968-400e-ae5b-49c4b9bba7e7.png)
Every worker processes one queue and interacts with one Sender.

To expand the service and add notification channels (sms, push, etc) use the Worker class and your own realization Sender class (AbstractSender).

## Deploy
To run the project:
1. Create .env (use template .env.example)
2. run command:
```docker-compose up --build```

## API documentation
Swagger:
    ```127.0.0.1:8000/api/openapi```

## Tests
To run tests:
1. Create file .env (use template .env.example)
2. Change the current directory to tests
3. run command:
```docker-compose up --build```
