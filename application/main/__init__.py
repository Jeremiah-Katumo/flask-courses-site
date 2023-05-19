# This implements application functionality in a blueprint.
# In single scripts applications, the application instance exists in the global scope, so routes can be easily defined
## ...using the app.route decorator. But in this case the application is created at runtime, the app.route decorator begins
### ...to exist only after create_app() is invoked, which is too late. Custom error pages handlers present the same problem,
#### ...as these are defined with the app.errorhandler decorator.

# A blueprint solves this problem as it is the same to an application in that it can also define routes and error handlers.
# The difference is that when these are defined in a blueprint they are in a dormant state until the blueprint is registered
## ...with an application, at this point they become part of it.
# Using a blueprint defined in the global scope, the routes and error handlers of the application can be defined in almost the 
# ...same way as in the single-script application.

from flask import Blueprint

# Blueprints are created by instantiating an object of class Blueprint. The constructor for this class taked two required arguments:
## 1) the blueprint name
## 2) the module or package where blueprint is located.
# As with applications, Python's __name__ variable is in most cases the correct value for the second argument.
main = Blueprint('main', __name__)

# NB: It is important to note that the modules are imported at the bottom of the app/main/__init__.py script to avoid errors due to circular dependencies.
from . import errors
from . import views
