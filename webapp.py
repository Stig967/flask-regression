from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'pawel_sliwa_interview_task' #required by html form.crsf_token
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///traffic.db'

traffic_db = SQLAlchemy(app)

#logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

# This file does not have to be used in the application
# Choice of the web server is up to the candidate

# Required endpoints:

from routes import *


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
