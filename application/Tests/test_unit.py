from flask_testing import TestCase
from application import app, db
from flask import url_for
from application.models import Players
from application.routes import *


class TestBase(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"
        app.config['SECRET_KEY'] = "secret"
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = True
        return app

    def setUp(self):
        db.create_all()

        test_player     =   Players(player_name="Player1", player_class="Test Class", level="51")
        test_player2    =   Players(player_name="Player2", player_class="Test Class", level="50")
        test_item       =   Items(item_name="Staff of Testing", value="200", weight="20", rarity="Rare", owner="1")
        test_item2      =   Items(item_name="Staff of Toasting", value="300", weight="10", rarity="Epic", owner="2")

        db.session.add(test_player)
        db.session.add(test_player2)
        db.session.add(test_item)
        db.session.add(test_item2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all

class TestViews(TestBase):
    def test_players_get(self):
        response = self.client.get(url_for("showplayers"))
        print(response.data)
        self.assertIn(b"Player1", response.data)
        self.assertEqual(response.status_code, 200)

class TestContinued(TestBase):
    def test_index_get(self):
        response = self.client.get(url_for("index"))
        self.assertIn(b"Player1", response.data)

    def test_addplayers(self):
        response = self.client.post(url_for("addplayers"),
        data = dict(player_name = "Player1", player_class = "Test Class", level="51"),
        follow_redirects = True)
        self.assertIn(b"Player1", response.data)

    def test_items(self):
        response = self.client.post(url_for('additems'),
        data = dict(item_name = "Staff of Testing", value = "200", weight="10"),
        follow_redirects = True)
        self.assertIn(b"Staff of Testing", response.data)
    
    def test_deleteplayers(self):
        self.client.get(url_for("deleteplayers", player_id="2"))
        player_no = Players.query.count()
        self.assertEqual(player_no, 8)

    def test_deleteitems(self):
        self.client.get(url_for("deleteitems", item_id="2"))
        item_no = Items.query.count()
        self.assertEqual(item_no, 5)

    def test_items_get(self):
        response = self.client.get(url_for("showitems"))
        print(response.data)
        self.assertIn(b"Staff of Testing", response.data)
        self.assertEqual(response.status_code, 200)