from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Todos
from application.forms import TodoForm, OrderTodo


@app.route('/', methods=['POST', 'GET'])
def index():