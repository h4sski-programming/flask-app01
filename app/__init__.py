from flask import Flask, render_template
import os


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)


#### Routes ####

@app.route('/')
def index():
    return render_template('index.html',
        value = 'value',
        number = 5,
        b = True,
        c = True,
        )

@app.route('/sam/')
def sam():
    modules_status = {
        'gps': True,
        'visual': True,
        'module_01': False,
        'module_02': True,
        'module_03': False,
    }
    return render_template('sam.html',
        value = 'value',
        modules_status = modules_status,
        )



#### debug and testing routes

@app.route('/test')
def test():
    return '<h1>test</h1>'


@app.route('/<int:number>')
def number2(number):
    return f'<h1>passed number = {number}</h1>'
