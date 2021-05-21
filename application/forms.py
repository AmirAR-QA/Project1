from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, validators
from wtforms.validators import DataRequired, ValidationError, Length 
from wtforms.fields.core import IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.models import Items, Players
from application import db

class PlayersForm(FlaskForm):
    player_name         =   StringField('Player Name', validators=[DataRequired()])
    player_class        =   StringField('Player Class', validators=[DataRequired()])
    level               =   IntegerField('Player level', validators=[DataRequired()])
    submit              =   SubmitField('Submit')
    update              =   SubmitField('Update')
    delete              =   SubmitField('Delete')

class ItemsForm(FlaskForm):
    item_name   =   StringField('Item Name', validators=[DataRequired(), Length(min=2,max=30)])
    value       =   StringField('Value (gp)', validators=[DataRequired()])
    weight      =   StringField('Weight (kg)', validators=[DataRequired()])
    rarity      =   StringField('Rarity', validators=[DataRequired()])
    submit      =   SubmitField('Submit')
    update      =   SubmitField('Update')
    delete      =   SubmitField('Delete')