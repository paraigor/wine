# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Установка

Скачайте код сайта.

Python3 должен быть установлен.  
С помощью команды `pip` (или `pip3`, если есть конфликт с Python2) установите необходимые библиотеки:
```
pip install -r requirements.txt
```

Скрипт генерирует главную страницу сайта подставляя данные из excel файла с винами в шаблон `template.html`.  
Образец файла `wine_example.xlsx` прилагается.  
Можно указать путь к файлу с винами в переменной окружения, в файле `.env`.
```
PATH_TO_WINES=wines.xlsx
```
Добавьте файлы изображений вина в папку `images`, если необходимо.

## Запуск

Запустите сайт командой
```
$ python3 main.py -p full/path/to/wine.xlsx
```
либо
```
$ python3 main.py --path full/path/to/wine.xlsx
```
Если путь к файлу с винами не передать в качестве аргумента, скрипт возьмет путь из переменной окружения `PATH_TO_WINES`.  
А если переменная окружения не задана, скрипт будет искать `wine.xlsx` в корне папки сайта.

Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).  
На странице будут представлены все вина из файла `wine.xlsx` разделенные на категории.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
