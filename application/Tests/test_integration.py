from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for
from application import app, db 
from application.models import Players, Items

class TestBase(LiveServerTestCase):
    def create_app(self):

        app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///test.db"
        app.config["LIVESERVER_PORT"] = 5050
        app.config['SECRET_KEY'] = "secret"
        app.config["DEBUG"]= True
        app.config["TESTING"]= True
        return app

    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        db.create_all()
        
        self.driver.get(f"http://localhost:5050")

    def tearDown(self):
        self.driver.quit()

        db.drop_all()

    def test_server_working(self):
        response = urlopen("http://localhost:5050")
        self.assertEqual(response.code, 200)

class TestViews(TestBase):

    def test_buttons_navigation(self):
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/a").click()

        self.assertIn(url_for("showplayers"), self.driver.current_url)
    
    def test_entries(self):
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr/td[4]/a").click()
        self.driver.find_element_by_xpath('//*[@id="player_name"]').send_keys("Player3")
        self.driver.find_element_by_xpath('//*[@id="player_class"]').send_keys("Tester")
        self.driver.find_element_by_xpath('//*[@id="level"]').send_keys("10")
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        players = Players.query.first()
        self.assertEqual(players.player_name, "Player3")

