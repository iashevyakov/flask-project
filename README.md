
1. Веб-сервер Nginx, сервер приложений uWSGI, базы данных PostgreSQL и Redis развернуты на 4-х контейнерах Docker.

2. **Внешние библиотеки**.

   _flask-login_ - для управления состоянием входа пользователя в систему.
   
   _flask-wtf_ - для создания форм в python-классах.
   
   _flask-sqlalchemy_ - для использования ORM (перевод python-кода в команды базы данных).
   
   _flask-migrate_ - для внесения изменений в базу данных с помощью python-кода.
   
   _psycopg2_ - для установления соединения с базой данных.
   
   _flask-and-redis_ - для использования ORM в Redis.
   
   _uwsgi_ - для настройки сервера приложений.
   
3. **Инструкция**.

   _git clone https://github.com/iashevyakov/test_task.git_
   
   _cd testtask_
   
   _sudo docker-compose up_
   
   _http://127.0.0.1:81/_
 
