from flask import Blueprint, flash, g, redirect, render_template


blueprint = Blueprint('routes', __name__)

@blueprint.route('/')
def index():
    return render_template('index.html')


@blueprint.route('/sam')
def sam():
    
    modules_status = {
        'gps': True,
        'vision': True,
        'scanning': False,
    }
    return render_template('sam.html', modules_status=modules_status)
