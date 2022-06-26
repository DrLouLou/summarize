from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'dg?9<6hGY`5Z|SG1!@WveMR|!~p$u+'

# Flask-Bootstrap requires this line
Bootstrap(app)

from app import routes
