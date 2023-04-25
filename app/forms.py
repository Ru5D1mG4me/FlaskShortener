from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired, URL


class URLForm(FlaskForm):
    original_url = StringField('Enter URL',
                               validators=[DataRequired(message='Field cannot be empty'),
                                           URL(message='Invalid URL')])
    submit = SubmitField('Shorten')