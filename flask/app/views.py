from app import app
from flask import Flask, render_template
from app.forms import MessagesForm
from app.rabbitmq import produce_messages

server = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MessagesForm()
    if form.validate_on_submit():
        produce_messages(
            message_body=form.message_body.data,
            message_amount=form.message_amount.data
        )
        
    return render_template(
        'index.html',
        form=form,
    )