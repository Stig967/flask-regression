from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'flask_regression'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///traffic.db'

traffic_db = SQLAlchemy(app)

#logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


from routes import *


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
