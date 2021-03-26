from django.test import TestCase
from .models import Image, Comment, Profile
from django.contrib.auth.models import User

class ImageTestClas(TestCase):
    def setUp(self):
        self.lorna = User(username = "ryan", email = "austinbrian005@gmail.com",password = "1234")
        self.food = Image(image = 'imageurl', name ='food', caption = 'Chicken Taco', profile = self.lorna)
        self.maua = Image(image = 'imageurl', name ='maua', caption = 'Lillies', profile = self.lorna)

        self.lorna.save()
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
        images = Image.get_profile_images(self.lorna)
        self.assertEqual(len(images),2)

class ProfileTestClas(TestCase):
    def setUp(self):
        self.lorna = User(username = "lorna", email = "lorna@gmail.com",password = "1234")
        self.lorna.save()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.lorna, User))

    def test_search_user(self):
        user = Profile.search_user(self.lorna)
        self.assertEqual(len(user), 1)