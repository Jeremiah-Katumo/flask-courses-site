"""Incomplete"""
# There are two main differences when writing a view function inside a blueprint.
# First, as was done for error handlers earlier, the route decorator comes from the blueprint,
## ...so 'main.route' is used instead of 'app.route'.
# The second difference is in the usage of url_for() function. The first argument to this function is 
## ...the endpoint name of the route, which for application-based routes defaults to the name of the view function.

# Namespace is applied to all the endpoints defined in a blueprint, so that blueprints can define view functions with
## ...the same endpoint names without collisions. The namespace is the name of the blueprint (the first argument to the blueprint constructor)
### ...and is separated from the endpoint name with a 'dot'. 

from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import LoginForm, RegisterForm
from .. import db
# from ..models import User

# @main.route('/', methods=['GET', 'POST'])
# def index():
#     form = LoginForm()
#     if form.validate_on_submit():
#         # ...
#         return redirect(url_for('.index'))
#     return render_template('index.html',
#     form=form, name=session.get('name'),
#     known=session.get('known', False),
#     current_time=datetime.utcnow())



# from . import app
from flask import render_template, request, json, Response, url_for, flash, redirect, session
from flask_login import login_user
from application.models import User, Course, Enrollment
# from application.main.forms import LoginForm, RegisterForm
# from flask_cachecontrol import cache, cache_for, dont_cache, Always, ResponseIsSuccessfulOrRedirect


# Create a data frame containing a subset of data to be inserted in the database
# courseData = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3","term":"Fall, Spring"}, 
#               {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"}, 
#               {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, 
#               {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, 
#               {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]


# The association between  a URL and the function that handles it is called a "route"
# A common use of decorators is to register functions as handler functions to be invoked
# when certain events occur.
# @app.route("/") are decorators


# The @app.route("/") decorator registers function index as the root URL.
# This also registers the index and home button
# The index() function in turn renders the index.html template.
@main.route("/")
@main.route("/index")
@main.route("/home")
def index():
    return render_template('index.html', index=True )


# # This view function creates a LoginForm object, it is imported from applications.forms.
# # The request is of type GET, the view function just renders the template, which in turn displays the form.
# # When the form is submitted in a POST request, Flask-WTF's validate_on_submit() function validates the form
# # ...variables, and then attempts to log the user.
# @main.route("/login", methods=['GET','POST'])
# def login():
#     if session.get('usernames'):
#         return redirect(url_for('index'))

#     form = LoginForm()
#     if form.validate_on_submit():
#         email      = form.email.data           # Create email variables obtained from the form
#         password   = form.password.data        # Create email variables obtained from the form

#         user       = User.query.filter_by(email=email).first()   # This line checks the first match of an email obtained from the users database.
#         # if user is not None and user.verify_password(password):
#         if user and user.get_password(password):
#             flash(f"{user.first_name}, you are succesfully logged in!", 'success')
#             session['user_id'] = user.user_id
#             session['username'] = user.first_name
#             return redirect("/index")
#         else:
#             # The login_user() function takes the user to log in and an optional "remember me" Boolean, which
#             # ...was also submitted with the form.
#             # A value of False for this argument causes the user session to expire when the browser window is closed, so
#             # ...the user will have to login in again next time.
#             # A value of True causes a long-term cookie to be set in the user's browser, which Flask-Login uses to restore the session.
#             # The optional REMEMBER_COOKIE_DURATION configuration option in config.py can be used to change the default one-year duration for the remeber cookie.
#             # The POST request that submitted the login credentials (email and password) ends with a redirect, but there are two possible URL destinations.
#             # If the login form was presented to the user to prevent unauthorized access to a protected URL the user wanted to visit, then Flask-Login will have saved
#             # ...that original URL in the 'next' query string argument, which can be accessed from the 'request.args' dictionary. If the 'next' query string argument 
#             # ...is not available, a redirect to the home page is issued instead. The URL in 'next' is validated to make sure it is a relative URL, to prevent a
#             # ...a malicious user from using this argument to redirect unsuspecting users to another site.
#             # login_user(user, form.remember_me.data)
#             # next = request.args.get('next')
#             # if next is None or not next.startswith('/'):
#             #     next = url_for('index.html')
#             # return redirect(next)
#             flash("Invalid Email or Password!", "danger")  # When the email adress or password is invalid, a flash message is set and the form is rendered again for the user to retry.
#     return render_template('login.html', title="Login", form=form, login=True )


# @main.route("/logout")
# def logout():
#     session['user_id']=False
#     session.pop('username',None)
#     return redirect(url_for('index'))


# @main.route("/courses/")
# @main.route("/courses/<term>")
# def courses(term=None):
#     if term is None:
#         term = "Spring 2019"
#         classes = Course.objects.order_by("-courseID")
#     return render_template('courses.html', courseData=courseData, courses = True, term=term )


# @main.route("/register", methods=['POST'])
# def register():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         user_id       =  User.objects.count()
#         user_id      +=  1

#         email         =  form.email.data
#         password      =  form.password.data
#         first_name    =  form.first_name.data
#         last_name     =  form.last_name.data

#         user = User(user_id, email=email, first_name=first_name, last_name=last_name)
#         user.set_password(password)
#         user.save()
#         # user.first_name in the flash() function confirms that the first_name has been registered.
#         flash(f"{ user.first_name }, you have successfully registered!", "success")
#         return redirect(url_for('/index'))
#     return render_template('register.html', title="Register", form=form, register=True)


# @main.route("/enrollment", methods=['GET', 'POST'])
# def enrollment():
#     if not session.get('username'):
#         return redirect(url_for())

#     id = request.form.get('courseID')
#     title = request.form['title']
#     term = request.form.get('term')
#     return render_template('enrollment.html', enrollment=True, data={"id":id,"title":title,"term":term})    


# @main.route("/api/")
# @main.route("/api/<idx>")
# def api(idx=None):
#     if(idx == None):
#         jdata = courseData
#     else:
#         jdata = courseData[int(idx)]
    
#     return Response(json.dumps(jdata), mimetype="application/json")


# # class User(db.Model):
# #     __tablename__ = 'users'

# #     user_id     =   db.Column( db.Integer, primary_key=True )
# #     first_name  =   db.Column( db.String(length=50) )
# #     last_name   =   db.Column( db.String(length=50) )
# #     email       =   db.Column( db.String(length=50) )
# #     password    =   db.Column( db.String(length=50) )


# # This route adds two instances of data to the user table created from models.py. It is imported from application.forms as 'User'.
# @main.route("/user")
# def user():
#     #User(user_id=1, first_name="Christian", last_name="Hur", email="christian@uta.com", password="abc1234").save()
#     #User(user_id=2, first_name="Mary", last_name="Jane", email="mary.jane@uta.com", password="password123").save()
#     users = User.objects.all()
#     #  users = Users(description=request.form['task-description'], project_id=project_id)
#     return render_template('user.html', users=users)

# # @app.after_request
# # def add_header(r):
# #     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
# #     r.headers["Pragma"] = "no-cache"
# #     r.headers["Expires"] = "0"
# #     r.headers["Cache-Control"] = 'public, max-age=0'
# #     return r
