
# import os
# from application import create_app, db
# from application.models import User, Course, Enrollment
# from flask_migrate import Migrate

# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# migrate = Migrate(app, db)

# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=db, User=User, Course=Course, Enrollment=Enrollment)

from application import app
