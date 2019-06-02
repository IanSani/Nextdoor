from django.test import TestCase
from .models import *
# Create your tests here.

class ProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id =1, username='zyzu')
        self.profile = Profile.objects.create(user = self.user,bio = 'blow away',email='abc@test.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_profile(self):
        self.profile.save()
        profile = Profile.get_profile()
        self.assertTrue(len(profile) > 0)

class HoodTest(TestCase):
    def setUp(self):
        self.Kinoo = Location.objects.create(name='Kinoo')

        self.south = Hood.objects.create(
            hood_name='south',occupants_count =1, location=self.Kinoo)

    def test_instance(self):
        self.south.save()
        self.assertTrue(isinstance(self.south, Hood))

    def test_get_hoods(self):
        self.south.save()
        hoods = Hood.get_hoods()
        self.assertTrue(len(hoods) > 0)
