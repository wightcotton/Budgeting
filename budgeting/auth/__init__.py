from flask import Blueprint

bp = Blueprint('auth', __name__)

from budgeting.auth import auth