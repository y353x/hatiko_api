## Сервис проверки imei устройств:
- бэкенд на Django с авторизацией JWT  
  эндпоинты:
   - /api/check-imei/
   - /auth/users/
   - /auth/jwt/create/
- интегрированный Телеграм Бот на библиотеке pyTelegramBotAPI

### Регистрация пользователя API-сервиса:
- POST запрос на эндпоинт /auth/users/ JSON:  
    {  
    "username": "your_username",  
    "password": "your_pass"  
    }  
### Получение JWT токена:
- POST запрос на эндпоинт /auth/jwt/create/ JSON:  
    {  
    "username": "your_username",  
    "password": "your_pass"  
    }  
  "access" токен из ответа используется  
  для запросов к эндпоинту /api/check-imei/

### Запрос проверки imei:
- POST запрос на эндпоинт /api/check-imei/ JSON:  
    {  
    "imei": your_device_imei,  
    "token": "api.imeicheck.net_token"  
    }  
    Авторизация Bearer Token.

### Запросы к Телеграм Боту:
- /start - проверка активности бота.
- imei - номер imei для проверки (15 символов)

## Запуск проекта:
- клонировать проект  
`git clone`
- создать .env файл по примеру .env.example
- создать образ Docker  
`docker build -t hatiko_backend . `
- запустить контейнер с образом  
`docker run -d --name hatiko_backend_container --rm -p 8000:8000 hatiko_backend`
- сделать миграции  
`docker exec hatiko_backend_container python manage.py migrate`
- запустить Телеграм Бот в контейнере  
`docker exec -d hatiko_backend_container python manage.py bot`
- API доступен локально по адресу http://127.0.0.1:8000/