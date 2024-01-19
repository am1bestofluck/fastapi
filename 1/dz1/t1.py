"""
Создать базовый шаблон для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню, подвал),
и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
 Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.
"""

from flask import Flask, render_template,url_for

app = Flask(__name__,template_folder="src",static_folder="src/css")
@app.route("/")
def root():
    return render_template("template.html")

@app.route("/about/")
def about():
    return render_template("specifics/about.html")


@app.route("/contacts/")
def contacts():
    return render_template("specifics/contacts.html")

@app.route("/shop/")
def shop():
    return render_template("specifics/shop.html")

@app.route("/shop/hats/")
def get_hats():
    return render_template("specifics/hats.html")

@app.route("/shop/jackets/")
def get_jackets():
    return render_template("specifics/jackets.html")

@app.route("/shop/shoes/")
def get_shoes():
    return render_template("specifics/shoes.html")

if __name__ == '__main__':
    app.run()