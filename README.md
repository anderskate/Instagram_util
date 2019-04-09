# Космический Instagram

Данный скрипт позволяет произвести автоматический сбор фотографий c последнего запуска ракеты SpaceX, а также фотографий с космического телескопа Hubble. Далее, с помощью библиотеки Instabot, производится автоматический постинг их в Instagram.

### Как установить

Для взаимодействия с API Instagram, необходимо авторизоваться. Необходимы логин и пароль от вашей учетной записи в Instagram.

Для этого создайте файл .env в папке проекта и запишите в нем логин и пароль, вот так:
```
LOGIN=[someLogin]
PASSWORD=[somePassword]
```
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Пример использования
Процесс скачивания изображений и загрузки в Instagram
```
(env) iMac-Andrej:instagram_api anderskate$ python main.py
Картинка 3838.jpg успешно скачана!
Картинка 3839.jpg успешно скачана!

...

2019-04-09 11:38:28,550 - INFO - Instabot Started
2019-04-09 11:38:29,971 - INFO - Logged-in successfully as 'amazing_space8'!
Analizing `images/3838.jpg`
FOUND w:4050, h:3240, ratio=1.25
Horizontal image
Resizing image
Saving new image w:1080 h:864 to `images/3838.jpg.CONVERTED.jpg`
FOUND: w:1080 h:864 r:1.25
2019-04-09 11:38:37,434 - INFO - Photo 'images/3838.jpg' is uploaded.
Analizing `images/3839.jpg`
FOUND w:4000, h:3200, ratio=1.25
Horizontal image
Resizing image
Saving new image w:1080 h:864 to `images/3839.jpg.CONVERTED.jpg`
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
