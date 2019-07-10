from budgeting.track_budget.model import model

from flask import (
    Blueprint, render_template
)

bp = Blueprint('track_budget', __name__, url_prefix='/track_budget', template_folder='templates')

data = model.Model()
budget_info = data.get_budget_info()
actuals_dict = data.get_accumulated_spending_by_category_by_month()
summary_dict = data.get_accumulated_spending_by_category()
past_year_dict = data.get_accumulated_spending_for_past_year()
super_cat_dict = data.get_accumulated_spending_by_super_category()

category_dict = model.Model().get_accumulated_spending_by_category()
transactions_dict = model.Model().get_transactions()

@bp.route('/monthly_drill_down')
def monthly_drill_down():
    return render_template('track_budget/monthly_drill_down.html',
                           actuals = actuals_dict,
                           budgets = budget_info,
                           summary = summary_dict,
                           past_year = past_year_dict,
                           super_categories = super_cat_dict,
                           categories = category_dict,
                           transactions = transactions_dict )

#@bp.route('/view_deltas')
#def view_deltas():
#    return render_template('track_budget/deltas.html', actuals = actuals_dict, budgets = budget_info)

#@bp.route('/view_summary')
#def view_summary():
#    return render_template('track_budget/summary.html', summary = summary_dict)