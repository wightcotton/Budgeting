from budgeting.track_budget.model import model

from flask import (
    Blueprint, render_template
)

bp = Blueprint('spending_analysis', __name__, url_prefix='/spending_analysis')

# data = model.Model()

@bp.route('/highlights')
def highlights():
    return render_template('spending_analysis/highlights.html' )

