Сервис проверки imei устройств:
- бэкенд на Django с авторизацией JWT
  эндпоинты:
   - /api/check-imei/
   - /auth/users/
   - /auth/jwt/create/
- интегрированный Телеграм Бот на библиотеке pyTelegramBotAPI

Регистрация пользователя API-сервиса:
- на эндпоинт /auth/users/ POST запрос с JSON:  
    {  
    "username": "your_username",  
    "password": "your_pass"  
    }  
Получение JWT токена:
- на эндпоинт /auth/jwt/create/ POST запрос с JSON:  
    {  
    "username": "your_username",  
    "password": "your_pass"  
    }  
  "access" токен из ответа используется  
  для запросов к эндпоинту /api/check-imei/

Запрос проверки imei:
- на эндпоинт /api/check-imei/ POST запрос с JSON:
    {
    "imei": your_device_imei,
    "token": "api.imeicheck.net_token"
    }
    Авторизация Bearer Token.

Запросы к Телеграм Боту:
- /start - проверка автивности бота.
- <imei> - номер imei для проверки (15 символов, без кавычек)