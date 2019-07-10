from budgeting.track_budget.model import get_trans_via_panda

from flask import (
    Blueprint, render_template
)

bp = Blueprint('transactions', __name__, url_prefix='/transactions')

@bp.route('/view_trans')
def view_trans():
    t = get_trans_via_panda.Transactions()
    return render_template('transactions/trans_list.html')

@bp.route('/tran_detail')
def tran_detail():
    t = get_trans_via_panda.Transactions()
    return render_template('transactions/tran_detail.html')