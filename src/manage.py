import os
import unittest
from app.main.model import user
from app.main.model import producttypes
from app.main.model import products
from app.main.model import paymentmethods
from app.main.model import customers

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main import create_app, db
from app.main import routes
app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.app_context().push()
#Adding additional routes
app.add_url_rule('/test', view_func=routes.test)
manager = Manager(app)
migrate = Migrate(app, db)
@manager.command
def run():
    app.run(debug=True, host='0.0.0.0')

#from app.main import create_app

#app = create_app()
@app.route('/')
def home():
   return "Hello Calculation World!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1
if __name__ == '__main__':
    manager.run()