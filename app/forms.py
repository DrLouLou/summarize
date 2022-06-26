from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SummarizeForm(FlaskForm):
    prompt = StringField('What Would You Like to Summarize?', validators=[DataRequired()])
    submit = SubmitField('Submit')
