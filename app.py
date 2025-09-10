from flask import Flask, url_for, request, redirect
from datetime import datetime

app=Flask(__name__)

@app.route("/")
def title_page():

    lab1 = url_for("start")

    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <header>
        НГТУ, ФБ, WEB-программирование часть 2
        <hr>
    </header>
    <main>
        <h1>Лабораторные работы по WEB-программированию</h1>

        <div class="menu"> 
            <ul>
                <li><a href="''' + lab1 + '''">Лабораторная работа #1</a></li>
            </ul>
        </div>
    </main>
    <footer>
        <hr>
        &copy;Саморуков Никита, ФБИ-34, 3 курс, 2025
    </footer>
</body>
</html>
'''

@app.route("/lab1/")
@app.route("/lab1/web")
def start():
    return"""<!doctype html>
        <html>
           <body>
               <h1>web-сервер на flask</h1>
           </body>
        </html>""", 200, {
            'X-Server': 'sample',
            'Content-Type': 'text/plain; charset=utf-8'
        }

@app.route("/lab1/author")
def author():

    name = "Саморуков Никита Олегович"
    group = "ФБИ-34"
    faculty = "ФБ"

    return"""<!doctype html>
        <html>
           <body>
               <p>Студент: """ + name + """</p>
               <p>Группа: """ + group + """</p>
               <p>Факультет: """ + faculty + """</p>
           </body>
        </html>"""

@app.route("/lab1/image")
def image():

    path = url_for("static", filename = "oak.jpg")
    style = url_for("static", filename = "lab1.css")

    return'''<!doctype html>
        <html>
           <head>
               <link rel="stylesheet" href="''' + style + '''">
           </head>
           <body>
               <h1>Дуб</h1>
                <img src="''' + path + '''">
           </body>
        </html>'''

count = 0

@app.route("/lab1/counter")
def counter():
    global count
    time = datetime.today()
    url = request.url
    client_ip = request.remote_addr
    counter_clear_route = url_for('clear_counter')

    count += 1

    return'''
<!doctype html>
    <html>
        <body>
            Сколько раз вы сюда заходили: ''' + str(count) + '''
            <hr>
            Дата и время: ''' + str(time) + '''
            <br> Запрошенный адрес: ''' + url + '''
            <br> Ваш IP адрес: ''' + client_ip + '''
            <br><a href="''' +  counter_clear_route + '''">Обнулить счетчик</a>
        </body>
    </html>
'''

@app.route("/lab1/counter/clear")
def clear_counter():
    global count
    count = 0

    return redirect("/lab1/counter")


@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/create")
def created():
    return'''
<!doctype html>
    <html>
        <body>
            <h1>Создано успешно!</h1>
            <div><i>Что-то создано...</i></div>
        </body>
    </html>
''', 201

@app.errorhandler(404)
def not_found(err):
    return "Такой страницы нет!"