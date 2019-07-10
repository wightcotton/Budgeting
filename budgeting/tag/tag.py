from budgeting.track_budget.model import get_trans_via_panda

from flask import (
    Blueprint, render_template
)

bp = Blueprint('tag', __name__, url_prefix='/tag')

@bp.route('/create_tag')
def create_tag():
    t = get_trans_via_panda.Transactions()
    return render_template('tag/create.html')

@bp.route('/show_tagged')
def show_tagged():
    t = get_trans_via_panda.Transactions()
    return render_template('tag/show_tagged.html')