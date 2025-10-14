from flask import Flask, url_for, request, redirect, abort, render_template
from datetime import datetime
from lab1 import lab1

from static.book_list import books
from static.flowers_list import flowers


app=Flask(__name__)
app.register_blueprint(lab1)


@app.route("/")
def title_page():

    lab1 = url_for("lab1")
    lab2 = url_for("lab2")

    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>НГТУ, ФБ, Лабораторные работы</title>
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
                <li><a href="''' + lab2 + '''">Лабораторная работа #2</a></li>
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

logger = []

@app.errorhandler(404)
def not_found(err):
    global logger
    now = datetime.today()
    logger.append(f"[{now.strftime("%Y-%m-%d %H:%M:%S")} пользователь {request.remote_addr}] перешел по адресу: {request.url}")
    logs = ""
    for i in logger:
        log = f"<li>{i}</li> "
        logs += log
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ошибка 404</title>
    <style>
        h1, h2 {
            font-size: 200px;
            color: violet;
            text-shadow: 5px 5px 10px purple;
            text-align: center;
            margin-bottom: 0;
            margin-top: 60px;
            animation: float 3s ease-in-out infinite;
        }

         h2 {
            font-size: 40px;
            text-shadow: none;
        }
        ul {
            list-style-type: none;
        }
        div.logger {
            position: fixed;
            bottom: 0px;
            left: 0px;
            color: green;
        }
    
        @keyframes float {
        0%   { transform: translateY(0px); }
        50%  { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
        }

    </style>
</head>
<body>
    <main>
        <h1>404</h1>
        <h2>Страница по запрашиваемому адресу не найдена</h2>
        <div class="logger">
            <ul>
                ''' + logs + '''
            </ul>
        </div>
    </main>
</body>
</html>
'''


@app.errorhandler(500)
def not_found(err):
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ошибка 500</title>
    <style>
        h1, h2 {
            font-size: 200px;
            color: grey;
            text-shadow: 5px 5px 10px black;
            text-align: center;
            margin-bottom: 0;
            margin-top: 60px;
        }

         h2 {
            font-size: 40px;
            text-shadow: none;
        }

    </style>
</head>
<body>
    <main>
        <h1>500</h1>
        <h2>Внутренняя ошибка сервера</h2>
    </main>
</body>
</html>
'''


@app.route('/lab2/a/')
def a_slash():
    return 'ok'


@app.route('/lab2/a')
def a():
    return 'ok'

flower_list = [{'name': 'роза', 'price': 400},
               {'name': 'тюльпан', 'price': 350},
               {'name': 'незабудка', 'price': 250},
               {'name': 'ромашка', 'price': 100}]

@app.route('/lab2/flowers/<int:flower_id>')
def flower_details(flower_id):
    if flower_id < 0 or flower_id >= len(flower_list):
        abort(404)
    else:
        return render_template('flower_info.html',
                                flower=flower_list[flower_id])


@app.route('/lab2/add_flower/')
@app.route('/lab2/add_flower/<name>/<int:price>')
def add_flower(name=None, price=0):
    if name:
        flower_list.append({'name': name, 'price': price})
        return render_template('flower_result.html', name=name, price=price, flower_list=flower_list, error=False)
    else:
        return render_template('flower_result.html', message="Вы не задали имя цветка", error=True), 400


@app.route('/lab2/flowers')
def list_flowers():
    return render_template('flower_all.html', flower_list=flower_list)


@app.route('/lab2/flowers/clear')
def clear_flowers():
    flower_list.clear()
    return render_template('flower_clear.html')


@app.route('/lab2/flowers/delete/<int:flower_id>')
def del_flower(flower_id):
    if flower_id < 0 or flower_id >= len(flower_list):
        abort(404)
    del flower_list[flower_id]
    return redirect(url_for('list_flowers'))


@app.route('/lab2/example')
def example():
    name = 'Саморуков Никита'
    group = 'ФБИ-34'
    lab = 2
    course = 3
    fruits = [{'name': 'яблоки', 'price': 150},
              {'name': 'персики', 'price': 250},
              {'name': 'бананы', 'price': 200}, 
              {'name': 'абрикосы', 'price': 200},
              {'name': 'манго', 'price': 300}]
    return render_template('example.html', name=name,
                                           group=group,
                                           lab=lab,
                                           course=course,
                                           fruits=fruits
                            )


@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')


@app.route('/lab2/filters')
def filters():
    phrase = 'О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных...'
    return render_template('filter.html',
                           phrase=phrase)


@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return f'''
<!doctype html>
<html>
  <body>
    <h1>Выражения</h1>
    <br> Суммирование: {a} + {b} = {a + b}
    <br> Вычитание: {a} - {b} = {a - b}
    <br> Умножение: {a} × {b} = {a * b}
    <br> Деление: {a} / {b} = {'Делить на 0 нельзя!' if b == 0 else a / b}
    <br> Возведение в с тепень: {a}<sup>{b}</sup> = {a ** b}
  </body>
</html>
'''


@app.route('/lab2/calc/')
def calc_default():
    return redirect('/lab2/calc/1/1')


@app.route('/lab2/calc/<int:a>')
def calc_missing(a):
    return redirect(f'/lab2/calc/{a}/1')



@app.route('/lab2/books')
def book_list():
    return render_template('books.html',
                           books=books)


@app.route('/lab2/tsvetochki')
def show_berries():
    return render_template('tsvetochki.html', items=flowers)
