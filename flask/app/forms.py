from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SubmitField
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired


class MessagesForm(FlaskForm):
    message_body = StringField(label='Message body',
                                 validators=[DataRequired()])
    message_amount = IntegerField(label='Amount of messages sent at once',
                                  validators=[DataRequired()])
    submit = SubmitField('Send messages')
