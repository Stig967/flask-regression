from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PredictionRequestForm(FlaskForm):
    #title = StringField('Tytul ale te walidowany',validators=[DataRequired()])
    predict_button = SubmitField('Request of predtiction')