import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'budgeting.sqlite')
    )
    app.config["EXPLAIN_TEMPLATE_LOADING"] = True

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

    from budgeting.auth import db
    db.init_app(app)

    from budgeting.auth import auth
    app.register_blueprint(auth.bp)

    from budgeting import home
    app.register_blueprint(home.bp)
    app.add_url_rule('/', endpoint='index')

    from budgeting.spending_analysis import spending_analysis
    app.register_blueprint(spending_analysis.bp)

    from budgeting.tag import tag
    app.register_blueprint(tag.bp)

    from budgeting.track_budget import track_budget
    app.register_blueprint(track_budget.bp)

    from budgeting.transactions import transactions
    app.register_blueprint(transactions.bp)

    output = []
    for rule in app.url_map.iter_rules():

        output.append(rule)

    for line in output:
        print( line)

    return app

# structure for the app
# URL                           template                            python view
# /                             home.index                          home
# /auth/register                auth.register                       auth
# /auth/login                   auth.login                          auth
# /transactions/view_trans      transactions.trans_list             transactions
# /transactions/tran_detail     transactions.tran_detail            transactions
# /track_budget/view_deltas     track_budget.deltas                 track_budget
# /track_budget/view_summary    track_budget.summary                track_budget
# /tag/create_tag               tag.create                          tag
# /tag/show_tagged              tag.show_tagged                     tag
