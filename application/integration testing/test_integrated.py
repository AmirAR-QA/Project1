from sqlite3 import dbapi2
from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for

from application import app.db 
from application.models import Players, Items

class TestBase(LiveServerTestCase):
    def create_app(self):

        app.config.["SQLALCHEMY_DATABASE_URI"]="sqlite:///test.db",
        app.config.["SQLALCHEMY_DATABASE_URI"]="sqlite:///test.db",
        app.config.["SQLALCHEMY_DATABASE_URI"]="sqlite:///test.db",
        app.config.["SQLALCHEMY_DATABASE_URI"]="sqlite:///test.db",
        app.config.["SQLALCHEMY_DATABASE_URI"]="sqlite:///test.db",
        return app

    def setUp(self):

        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)

        db.session.add()
        db.session.commit()

        self.driver.get(f'http://localhost:{5050}')

    def tearDown(self):
        self.driver.quit()

        db.drop_all()

class TestStories(TestBase):
    def test_add_new_game(self):