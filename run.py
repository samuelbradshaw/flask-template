from main import app

# Returns true when run from terminal: `python3 run.py`
if __name__ == '__main__':
  app.jinja_env.auto_reload=True
  app.run(debug=True, host='127.0.0.1', port=8080, threaded=False)
