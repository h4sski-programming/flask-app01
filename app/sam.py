from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from app.auth import login_required
from app.db import get_db

blueprint = Blueprint('blog', __name__)


@blueprint.route('/')
def index():
    db = get_db()