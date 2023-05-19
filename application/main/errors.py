from flask import render_template, jsonify, request
from . import main                  # main is imported from app/main/__init__.py
from flask_cachecontrol import dont_cache

# Error handlers return a response, like view functions, but they also need to return the numeric status code
## ...that corresponds to the error, which Flask conveniently accepts as a second return value.
# The templates refrenced in the error handler functions must be written in the same layout as the regular pages, so
## ...in this case they will have a navigation bar and a page header that shows the error message.
@main.app_errorhandler(403)
@dont_cache()
def forbidden(e):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'forbidden'})
        response.status_code = 403
        return response
    return render_template('403.html'), 403


@main.app_errorhandler(404)
@dont_cache()
def page_not_found(e):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    return render_template('404.html'), 404


@main.app_errorhandler(500)
@dont_cache()
def internal_server_error(e):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'internal server error'})
        response.status_code = 500
        return response
    return render_template('500.html'), 500


# @main.app_errorhandler(304)
# @dont_cache
# def page_not_modified(e):
#     if request.accept_mimetypes.accept_json and \
#             not request.accept_mimetypes.accept_html:
#         response = jsonify({'error': 'page not modified'})
#         response.status_code = 304
#         return response
#     return render_template('304.html'), 304

# A difference when writing error handlers inside a blueprint is that if the 'errorhandler' decorator is used, 
# ...the handler will be invoked only for errors that originate in the routes defined by the blueprint. 
# To install application-wide error handlers, the 'app_errorhandler' decorator must be used instead
