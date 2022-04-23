from unittest import TestCase
from app import app
from models import User, db

DEFAULT_TEST_IMG = "https://image.shutterstock.com/image-photo/cheerful-hipster-guy-smiles-happily-600w-744198382.jpg"


def init_data():
    user = User(first_name="TestFirst", last_name="TestLast")
    db.session.add(user)
    db.session.flush()

    return user

class UserViewsRouteTests(TestCase):
    def setUp(self):
        """Stuff to do before every test."""
        
        User.query.delete()
        # check if I can delete posts along with users (create new post-> assign to user -> delete user -> try to fetch user and posts)
        
        user = init_data()
        
        self.full_name = user.full_name
        self.user_id = user.id

    def tearDown(self):
        """Clean up any weird transactions"""
        db.session.rollback()

    def test_root_dir(self):
        with app.test_client() as client:
            resp = client.get('/')
            self.assertEqual(resp.status_code, 302)
    
    def test_home_page(self):
        with app.test_client() as client:
             resp = client.get('/users')
             html = resp.get_data(as_text=True)

             self.assertEqual(resp.status_code, 200)
             self.assertIn('TestFirst', html)
    
    def test_user_profile(self):
        with app.test_client() as client:
            resp = client.get(f"/users/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(f'<h1>{self.full_name}</h1>',html)
    
    def test_add_new_user(self):
        with app.test_client() as client:
            d = {"first_name": "Daniel", "last_name": "Levin", "image_url": DEFAULT_TEST_IMG}
            resp = client.post("/users/new", data= d, follow_redirects = True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(f"{self.full_name}", html)
