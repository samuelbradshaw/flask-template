# Third-party libraries
from flask import Flask

app = Flask(__name__)

from main import views
