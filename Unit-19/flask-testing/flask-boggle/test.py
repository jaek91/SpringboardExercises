from unittest import TestCase
from app import app
from flask import session


app.config["TESTING"] = True


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature! 
    def setUp(self):
        """What we run before every test"""
        self.client = app.test_client()
        app.config["TESTING"] = True
    
    def test_homepage(self):
        with self.client:
            response = self.client.get('/')
            self.assertIn('board', session)
            self.assertIsNone(session.get('numplays'))
            self.assertIn(b'Score:', response.data)
            self.assertIn(b'Seconds Left:', response.data)

    def test_valid_word(self):
        """Test if word is valid by modifying the board in the session"""

        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["D", "A", "D", "D", "D"], 
                                ["D", "A", "D", "D", "D"], 
                                ["D", "A", "D", "D", "D"], 
                                ["D", "A", "D", "D", "D"], 
                                ["D", "A", "D", "D", "D"]]
        response = self.client.get('/check-word?word=dad')
        self.assertEqual(response.json['result'], 'ok')

    def test_invalid_word(self):
        """Test what output we get for an invalid word"""
        self.client.get('/')
        response = self.client.get('/check-word?word=elephant')
        self.assertEqual(response.json['result'],'not-on-board')

    def test_non_english_word(self):
        """Test that a nonsensical word is not on the board"""

        self.client.get('/')
        response = self.client.get(
            '/check-word?word=fsdfsdfsdfsawksf')
        self.assertEqual(response.json['result'], 'not-word')