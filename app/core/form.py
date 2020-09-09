from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class CreateDeleteEmail(FlaskForm):
    """Form for add or delete email"""

    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')
