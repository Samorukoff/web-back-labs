from flask import Blueprint, render_template, request, make_response, redirect


lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name,
                                        name_color = name_color)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'cornflowerblue')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user,
                                              age=age,
                                              sex=sex,
                                              errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    elif drink == 'green-tea':
        price = 70
    else:
        price = 0

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('lab3/pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    price = request.args.get('price')
    return render_template('lab3/success.html', price=price)


@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    size = request.args.get('size')
    background_color = request.args.get('background_color')
    font_style = request.args.get('font_style')
    if color or size:
        resp = make_response(redirect('/lab3/settings'))
        resp.set_cookie('color', color)
        resp.set_cookie('size', size)
        resp.set_cookie('background_color', background_color)
        resp.set_cookie('font_style', font_style)
        return resp

    color = request.cookies.get('color')
    size = request.cookies.get('size')
    background_color = request.cookies.get('background_color')
    font_style = request.cookies.get('font_style')
    resp = make_response(render_template('lab3/settings.html', color=color,
                                         size=size,
                                         background_color=background_color,
                                         font_style=font_style))
    return resp