from flask import Flask, render_template,redirect,flash,url_for
from config import Config
from forms import LoginForm
app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Gabriel'}
    posts = [
        {
            'author': {'username': 'Gabriel'},
            'body': 'Amanheceu um dia chuvoso em Campina Grande!'
        },
        {
            'author': {'username': 'Daniel'},
            'body': 'Acordei disposto a trabalhar!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
if __name__ == "__main__":
    app.run(debug=True)