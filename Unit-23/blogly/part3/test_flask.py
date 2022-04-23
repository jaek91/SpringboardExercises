from unittest import TestCase
from app import app
from models import User, Post, Tag, PostTag, db

DEFAULT_TEST_IMG = "https://image.shutterstock.com/image-photo/cheerful-hipster-guy-smiles-happily-600w-744198382.jpg"


def init_data():
    user = User(first_name="TestFirst", last_name="TestLast")
    db.session.add(user)
    db.session.flush()

    post = Post(title="Test Post", content = "This is great content", user_id = user.id)
    db.session.add(post)
    db.session.flush()

    tag = Tag(name="fun")
    db.session.add(tag)
    db.session.flush()

    posttag = PostTag(post_id = post.id, tag_id = tag.id)
    db.session.add(posttag)

    db.session.commit()

    return [user,post]

class UserViewsRouteTests(TestCase):
    def setUp(self):
        """Stuff to do before every test."""
        PostTag.query.delete()
        Tag.query.delete()
        Post.query.delete()
        User.query.delete()
        
        database_classes = init_data()
        user = database_classes[0]
        post = database_classes[1]

        self.full_name = user.full_name
        self.user_id = user.id
       
        self.post_id = post.id

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

    def test_get_posts(self):
        with app.test_client() as client:
            resp = client.get(f"/posts/{self.post_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(f"{self.full_name}", html)
    
    def test_edit_posts(self):
        with app.test_client() as client:
            edited_post = {"title": "Completely edited post title", "content": "wow, look it's newly edited"}
            resp = client.post(f"/posts/{self.post_id}/edit", data = edited_post, follow_redirects = True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(edited_post["title"], html)
    