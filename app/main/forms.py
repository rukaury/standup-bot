from flask_wtf import FlaskForm
from wtforms import TextAreaField, DateField, validators
from wtforms.validators import DataRequired

class StandupForm(FlaskForm):
    date = DateField('Post on', validators=[DataRequired()], format='%Y-%m-%d')
    today_tasks = TextAreaField(u'Today tasks', [validators.required(), validators.length(max=500)])
    yesterday_tasks = TextAreaField(u'Yesterday tasks', [validators.required(), validators.length(max=500)])
    additional_info = TextAreaField(u'Additional info', [validators.required(), validators.length(max=500)])