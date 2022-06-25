from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SummarizeForm(FlaskForm):
    prompt = StringField('What would you like to summarize?', validators=[DataRequired()])
    submit = SubmitField('Submit')