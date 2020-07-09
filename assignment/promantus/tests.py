from django.test import TestCase
from .models import UserProfile


# Create your tests here.

class UserProfileTests(TestCase):
    def setUp(self):
        UserProfile.objects.create(name="Kshitij", data={"age": 28, "address": "Dehradun"})
        UserProfile.objects.create(name="Anup", data={"age": 30, "address": "Delhi"})

    def test_user_profile_details(self):
        """User details are correctly identified"""
        kj = UserProfile.objects.get(name="Kshitij")
        aj = UserProfile.objects.get(name="Anup")
        self.assertIs(kj.data, {"age": 28, "address": "Dehradun"})
        self.assertIs(aj.data, {"age": 30, "address": "Delhi"})
