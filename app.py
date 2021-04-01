from flask import Flask, render_template, jsonify, request, flash, redirect, url_for
from forms import MessageForm
import os

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

current_message = 'Hello!'

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    global current_message
    form = MessageForm()
    if form.validate_on_submit():
        message = form.message.data
        current_message = message[:16]
        flash(f'Your message \'{current_message}\' has been submitted and will be displayed shortly!', 'success')
        return redirect(url_for('home'))
    return render_template('index.html', form=form, current_message=current_message)

@app.route('/message')
def get_message():
    return current_message

if __name__ == '__main__':
    app.run(debug=False)
