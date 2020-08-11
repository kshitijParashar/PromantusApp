from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class SignUpTest(TestCase):
    """first test with allowed Host"""
    def test_should_respond_only_for_example_a(self):
        client = Client(HTTP_HOST="example-A.com")
        view = reverse("signup")
        response = client.get(view)
        self.assertEqual(response.status_code, 200)

    """Second test with allowed Host"""
    def test_should_not_respond_for_example_b(self):
        client = Client(HTTP_HOST="www.example-B.com")
        view = reverse("signup")
        response = client.get(view)
        self.assertEqual(response.status_code, 400)

    """Third test with allowed Host"""
    def test_should_not_respond_for_example_c(self):
        client = Client(HTTP_HOST="www.example-C.com")
        view = reverse("signup")
        response = client.get(view)
        self.assertEqual(response.status_code, 400)

    """forth test with non-allowed Host"""
    def test_should_not_respond_for_example_d(self):
        client = Client(HTTP_HOST="www.example-D.com")
        view = reverse("signup")
        response = client.get(view)
        self.assertEqual(response.status_code, 400)
        
    """fifth test with non-allowed Host"""
    def test_should_not_respond_for_example_e(self):
        client = Client(HTTP_HOST="www.example-E.com")
        view = reverse("signup")
        response = client.get(view)
        self.assertEqual(response.status_code, 200)