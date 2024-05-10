import random
facts_list = []

from flask import Flask


app = Flask(__name__)
@app.route("/ПУТЬ")
def НАЗВАНИЕ_ФУНКЦИИ():


@app.route("/")
def hello_world():

    return '<h1>Hello, World!</h1>'

return f'<p>{random.choice(facts_list)}</p>'


app.run(debug=True)
