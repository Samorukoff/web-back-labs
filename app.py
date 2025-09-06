from flask import Flask, url_for, request, redirect
from datetime import datetime

app=Flask(__name__)

@app.route("/")
@app.route("/web")
def start():
    return"""<!doctype html>
        <html>
           <body>
               <h1>web-сервер на flask</h1>
           </body>
        </html>"""

@app.route("/author")
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

@app.route("/image")
def image():

    path = url_for("static", filename= "oak.jpg")

    return'''<!doctype html>
        <html>
           <body>
               <h1>Дуб</h1>
               <img src="''' + path + '''">
           </body>
        </html>'''

count = 0

@app.route("/counter")
def counter():
    global count
    time = datetime.today()
    url = request.url
    client_ip = request.remote_addr

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
        </body>
    </html>
'''

@app.route("/info")
def info():
    return redirect("/author")