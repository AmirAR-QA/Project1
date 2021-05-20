from application import app, db
from flask import render_template, redirect, url_for
from application.models import Items, Players
from application.forms import PlayersForm, ItemsForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    all_players = Players.query.all()
    all_items = Items.query.all()
    return render_template('body.html', Items=all_items, player_list = all_players)

@app.route('/editplayers', methods=["GET", "POST"])
def editplayers():
    form = PlayersForm()
    if form.validate_on_submit():
        edit_player = Player(player_name = form.player_name.data)
        db.session.add(edit_player)
        db.session.commit()
        return redirect('index')
    return render_template('editplayers.html', form=form)