from django.test import TestCase
from .models import Image, Comment, Profile
from django.contrib.auth.models import User

class ImageTestClas(TestCase):
    def setUp(self):
        self.ryan = User(username = "ryan", email = "ryan@gmail.com",password = "1234")
        self.food = Image(image = 'imageurl', name ='food', caption = 'Chicken Taco', profile = self.ryan)
        self.maua = Image(image = 'imageurl', name ='maua', caption = 'Lillies', profile = self.ryan)

        self.ryan.save()
        self.food.save_image()

    def tearDown(self):
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.food, Image))

    def test_save_image_method(self):
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)

    def test_delete_image(self):
        images1 = Image.objects.all()
        self.assertEqual(len(images1),1)
        self.food.delete_image()
        images2 = Image.objects.all()
        self.assertEqual(len(images2),0)

    def test_update_caption(self):
        self.food.update_caption('Bolognese')
        self.assertEqual(self.food.caption, 'Bolognese')

    def test_get_profile_images(self):
        self.maua.save_image()
        images = Image.get_profile_images(self.ryan)
        self.assertEqual(len(images),2)

class ProfileTestClas(TestCase):
    def setUp(self):
        self.ryan = User(username = "ryan", email = "ryan@gmail.com",password = "1234")
        self.ryan.save()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.ryan, User))

    def test_search_user(self):
        user = Profile.search_user(self.ryan)
        self.assertEqual(len(user), 1)

class CommentTestClas(TestCase):
    def setUp(self):
        self.ryan = User(username = "ryan", email = "ryan@gmail.com",password = "1234")
        self.food = Image(image = 'imageurl', name ='food', caption = 'Chicken Taco', profile = self.ryan)
        self.comment = Comment(image=self.food, content= 'Looks delicious', user = self.ryan)

        self.ryan.save()
        self.food.save_image()
        self.comment.save_comment()

    def tearDown(self):
        Image.objects.all().delete()
        Comment.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        comments = Comment.objects.all()
        self.assertTrue(len(comments)> 0)

    def test_delete_comment(self):
        comments1 = Comment.objects.all()
        self.assertEqual(len(comments1),1)
        self.comment.delete_comment()
        comments2 = Comment.objects.all()
        self.assertEqual(len(comments2),0)

    def test_get_image_comments(self):
        comments = Comment.get_image_comments(self.food)
        self.assertEqual(comments[0].content, 'Looks delicious')
        self.assertTrue(len(comments) > 0)