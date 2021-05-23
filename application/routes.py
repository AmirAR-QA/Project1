from application import app, db
from flask import render_template, redirect, url_for, request
from application.models import Items, Players
from application.forms import PlayersForm, ItemsForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    form2 = ItemsForm()
    items_sorted  = Items.query.order_by(Items.item_id).all() 
    return render_template("index.html", form=form2, all_items=items_sorted, title="What's yours is mine c:")

@app.route('/addplayers', methods=["GET", "POST"])
def addplayers():
    form = PlayersForm()
    error = ""
    if request.method == "POST":
        value1 = form.player_name.data
        value2 = form.player_class.data
        value3 = form.level.data
        added_player = Players(player_name = value1, player_class = value2, level = value3)
        db.session.add(added_player)
        db.session.commit()
        if form.validate_on_submit():
            return redirect('index')
    return render_template('addplayers.html', form=form, title="A list of all your potential enemies...")

@app.route('/additems', methods=["GET", "POST"])
def additems():
    form = ItemsForm()
    error = ""
    if request.method == "POST":
        value1 = form.item_name.data
        value2 = form.value.data
        value3 = form.weight.data
        value4 = form.rarity.data
        added_item = Items(item_name = value1, value = value2, weight = value3, rarity = value4)
        db.session.add(added_item)
        db.session.commit()
        if form.validate_on_submit():
            return redirect('index')
    return render_template('additems.html', form=form, title="Encumbered in 3... 2... 1...")

@app.route("/players", methods=["GET", "POST"])
def showplayers():
    form = PlayersForm()
    players_sorted  = Players.query.order_by(Players.player_id).all() 
    return render_template("players.html", form=form, all_players=players_sorted, title="The Fellowship")

@app.route('/deleteplayers/<int:player_id>')
def deleteplayers(player_id):
    deleted_player = Players.query.get(player_id)
    db.session.delete(deleted_player)
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/items", methods=["GET", "POST"])
def showitems():
    form = ItemsForm()
    items_sorted  = Items.query.order_by(Items.item_id).all() 
    return render_template("items.html", form=form, title='So you found a stick', all_items=items_sorted)

@app.route('/deleteitems/<int:item_id>')
def deleteitems(item_id):
    deleted_item = Items.query.get(item_id)
    db.session.delete(deleted_item)
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/updateplayers/<player_id>", methods=['GET', 'POST'])
def update_player(player_id):
    player = db.session.query(Players).get(player_id)
    form = PlayersForm(obj=player)
    if form.validate_on_submit():
        form.populate_obj(player)
        db.session.add(player)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('updateplayers.html', title="Level up!", form=form)

@app.route("/updateitems/<item_id>", methods=['GET', 'POST'])
def update_item(item_id):
    item = db.session.query(Items).get(item_id)
    form = ItemsForm(obj=item)
    if form.validate_on_submit():
        form.populate_obj(item)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('updateitems.html', title="Equip fireba- No wait!", form=form)