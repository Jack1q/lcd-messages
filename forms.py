from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField

class MessageForm(FlaskForm):
    message = StringField('Message', validators=[DataRequired(), Length(min=1,max=15)])
    submit = SubmitField('Post')