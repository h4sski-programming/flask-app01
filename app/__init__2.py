import os
from flask import Flask, render_template

# copy paste from https://flask.palletsprojects.com/en/2.3.x/tutorial/factory/
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='h4sski',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass




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

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return '<h1>Hello, World!</h1>'
    
    from . import db, auth
    db.init_app(app)
    app.register_blueprint(auth.bp)
    
    return app