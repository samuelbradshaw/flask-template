# Python standard libraries

# Third-party libraries
from flask import Flask, render_template, request, redirect, send_from_directory, abort

# Internal imports
from main import app, config, db


# Variables injected into all templates
@app.context_processor
def inject_common_variables():
  site_name = config.SITE_NAME
  app_root = request.url_root.rstrip('/')
  forced_theme = request.args.get('theme', 'default')
  return dict(site_name=site_name, app_root=app_root, forced_theme=forced_theme)


# ROUTES

@app.route('/')
def content_home():
  breadcrumbs = []
  page = {
    'title': config.SITE_NAME,
    'breadcrumb_title': 'Home',
    'description': 'This is a Python Flask sample project.',
    'request': request,
    'site_section': 'home',
    'breadcrumbs': breadcrumbs,
    'siblings': {},
  }
  return render_template('/home.html', page=page)


@app.route('/test-db')
def content_test_db():

  try:
    database_name = db.lookup_one('''
      SELECT DATABASE() FROM DUAL
    ''')['DATABASE()']
    error_message = None
  except Exception as e:
    database_name = None
    error_message = e

  breadcrumbs = []
  breadcrumbs.append({'title': 'Home', 'href': '/',})
  siblings = []
  page = {
    'title': 'Test Database',
    'breadcrumb_title': 'Test Database',
    'description': '',
    'request': request,
    'site_section': 'test',
    'breadcrumbs': breadcrumbs,
    'siblings': {},
  }
  return render_template('/test-db.html', page=page, database_name=database_name, error_message=error_message)


# UTILITY ROUTES

# robots.txt
@app.route('/.well-known/<filename>')
def static_from_root(filename):
  return send_from_directory(app.static_folder, '_well-known/{0}'.format(filename))

# Handle errors
@app.errorhandler(400) # Bad Request
@app.errorhandler(401) # Unauthorized (not signed in)
@app.errorhandler(403) # Forbidden (signed in but not authorized)
@app.errorhandler(404) # Not Found
@app.errorhandler(500) # Internal Server Error
def show_error(error):
  breadcrumbs = []
  breadcrumbs.append({'title': 'Home', 'href': '/',})
  page = {
    'title': '{0}: Error'.format(config.SITE_NAME),
    'breadcrumb_title': 'Error',
    'url': request.path,
    'breadcrumbs': breadcrumbs,
  }
  return render_template('/error.html', page=page, error=error), error.code

# Test errors
@app.route('/error/<code>')
def simulate_error(code):
  abort(int(code))


# Close the database connection after the request finishes
@app.after_request
def after_request(response):
  db.close_connection()
  return response
